# Copyright 2021 Flower Labs GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Ray-based Flower ClientProxy implementation."""


import traceback
from logging import ERROR
from typing import Optional

from flwr import common
from flwr.client import ClientFnExt
from flwr.client.client_app import ClientApp
from flwr.client.run_info_store import DeprecatedRunInfoStore
from flwr.common import DEFAULT_TTL, Message, Metadata, RecordSet
from flwr.common.constant import (
    NUM_PARTITIONS_KEY,
    PARTITION_ID_KEY,
    MessageType,
    MessageTypeLegacy,
)
from flwr.common.logger import log
from flwr.common.recordset_compat import (
    evaluateins_to_recordset,
    fitins_to_recordset,
    getparametersins_to_recordset,
    getpropertiesins_to_recordset,
    recordset_to_evaluateres,
    recordset_to_fitres,
    recordset_to_getparametersres,
    recordset_to_getpropertiesres,
)
from flwr.server.client_proxy import ClientProxy
from flwr.simulation.ray_transport.ray_actor import VirtualClientEngineActorPool


class RayActorClientProxy(ClientProxy):
    """Flower client proxy which delegates work using Ray."""

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments
        self,
        client_fn: ClientFnExt,
        node_id: int,
        partition_id: int,
        num_partitions: int,
        actor_pool: VirtualClientEngineActorPool,
    ):
        super().__init__(cid=str(node_id))
        self.node_id = node_id
        self.partition_id = partition_id # range(num_clients)

        def _load_app() -> ClientApp:
            return ClientApp(client_fn=client_fn)

        self.app_fn = _load_app
        self.actor_pool = actor_pool
        self.proxy_state = DeprecatedRunInfoStore(
            node_id=node_id,
            node_config={
                PARTITION_ID_KEY: str(partition_id),
                NUM_PARTITIONS_KEY: str(num_partitions),
            },
        )

    def _submit_job(self, message: Message, timeout: Optional[float]) -> Message:
        """Sumbit a message to the ActorPool."""
        run_id = message.metadata.run_id

        # Register state
        self.proxy_state.register_context(run_id=run_id)

        # Retrieve context
        context = self.proxy_state.retrieve_context(run_id=run_id)
        partition_id_str = str(context.node_config[PARTITION_ID_KEY]) # only for ray.actorpool to trace the future

        # edit message and context for logging
        def get_msg_type(message: Message) -> str:
            if message.metadata.message_type == MessageType.TRAIN:
                return "training"
            if message.metadata.message_type == MessageType.EVALUATE:
                return "evaluating"
            else:
                return "x"
        def append_cid_and_round_num(message: Message, cid, round_num) -> None:
            for k, v in message.content.configs_records.items():
                if k in ["fitins.config", "evaluateins.config"]:
                    v["cid"] = cid
                    v["round_num"] = round_num
                
        msg_type = get_msg_type(message)
        round_num = str(message.metadata.group_id)
        original_cid = str(context.node_config['partition-id']) # remember to restore
        context.node_config['partition-id'] = "{}!!!{}!!!{}".format(msg_type, original_cid, round_num)
        append_cid_and_round_num(message, original_cid, round_num)

        try:
            self.actor_pool.submit_client_job(
                lambda a, a_fn, mssg, partition_id, context: a.run.remote(
                    a_fn, mssg, partition_id, context
                ), # actor_fn
                (self.app_fn, message, partition_id_str, context), # job: tuple[ClientAppFn, Message, str, Context]
            )
            out_mssg, updated_context = self.actor_pool.get_client_result(
                partition_id_str, timeout
            )
            updated_context.node_config['partition-id'] = original_cid # restore partition-id (original_cid)

            # Update state
            self.proxy_state.update_context(run_id=run_id, context=updated_context)

        except Exception as ex:
            if self.actor_pool.num_actors == 0:
                # At this point we want to stop the simulation.
                # since no more client runs will be executed
                log(ERROR, "ActorPool is empty!!!")
            log(ERROR, traceback.format_exc())
            log(ERROR, ex)
            raise ex

        return out_mssg

    def _wrap_recordset_in_message(
        self,
        recordset: RecordSet,
        message_type: str,
        timeout: Optional[float],
        group_id: Optional[int],
    ) -> Message:
        """Wrap a RecordSet inside a Message."""
        return Message(
            content=recordset,
            metadata=Metadata(
                run_id=0,
                message_id="",
                group_id=str(group_id) if group_id is not None else "",
                src_node_id=0,
                dst_node_id=self.node_id,
                reply_to_message="",
                ttl=timeout if timeout else DEFAULT_TTL,
                message_type=message_type,
            ),
        )

    def get_properties(
        self,
        ins: common.GetPropertiesIns,
        timeout: Optional[float],
        group_id: Optional[int],
    ) -> common.GetPropertiesRes:
        """Return client's properties."""
        recordset = getpropertiesins_to_recordset(ins)
        message = self._wrap_recordset_in_message(
            recordset,
            message_type=MessageTypeLegacy.GET_PROPERTIES,
            timeout=timeout,
            group_id=group_id,
        )

        message_out = self._submit_job(message, timeout)

        return recordset_to_getpropertiesres(message_out.content)

    def get_parameters(
        self,
        ins: common.GetParametersIns,
        timeout: Optional[float],
        group_id: Optional[int],
    ) -> common.GetParametersRes:
        """Return the current local model parameters."""
        recordset = getparametersins_to_recordset(ins)
        message = self._wrap_recordset_in_message(
            recordset,
            message_type=MessageTypeLegacy.GET_PARAMETERS,
            timeout=timeout,
            group_id=group_id,
        )

        message_out = self._submit_job(message, timeout)

        return recordset_to_getparametersres(message_out.content, keep_input=False)

    def fit(
        self, ins: common.FitIns, timeout: Optional[float], group_id: Optional[int]
    ) -> common.FitRes:
        """Train model parameters on the locally held dataset."""
        recordset = fitins_to_recordset(
            ins, keep_input=True
        )  # This must stay TRUE since ins are in-memory
        message = self._wrap_recordset_in_message(
            recordset,
            message_type=MessageType.TRAIN,
            timeout=timeout,
            group_id=group_id, # group_id is round_num (training starts from round#1)
        )

        message_out = self._submit_job(message, timeout)

        return recordset_to_fitres(message_out.content, keep_input=False)

    def evaluate(
        self, ins: common.EvaluateIns, timeout: Optional[float], group_id: Optional[int]
    ) -> common.EvaluateRes:
        """Evaluate model parameters on the locally held dataset."""
        recordset = evaluateins_to_recordset(
            ins, keep_input=True
        )  # This must stay TRUE since ins are in-memory
        message = self._wrap_recordset_in_message(
            recordset,
            message_type=MessageType.EVALUATE,
            timeout=timeout,
            group_id=group_id,
        )

        message_out = self._submit_job(message, timeout)

        return recordset_to_evaluateres(message_out.content)

    def reconnect(
        self,
        ins: common.ReconnectIns,
        timeout: Optional[float],
        group_id: Optional[int],
    ) -> common.DisconnectRes:
        """Disconnect and (optionally) reconnect later."""
        return common.DisconnectRes(reason="")  # Nothing to do here (yet)
