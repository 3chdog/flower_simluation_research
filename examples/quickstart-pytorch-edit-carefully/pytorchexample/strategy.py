import os
import numpy as np
from typing import Optional, Union
from flwr.common import (
    FitRes,
    Parameters,
    Scalar,
    parameters_to_ndarrays
)
from flwr.server.client_proxy import ClientProxy
from flwr.server.strategy import FedAvg

def on_fit_config(server_round: int):
    """Construct `config` that clients receive when running `fit()`"""
    return {"round_num": server_round}

def is_saving(saving_period: Optional[int], server_round: int, num_rounds: int):
    if saving_period is None:
        return False
    if server_round == num_rounds:
        return True
    if server_round % saving_period == 0:
        return True
    return False

class FedAvgWithSaving(FedAvg):
    def __init__(self, info_for_model_saving: dict = {}, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.info_for_model_saving = info_for_model_saving

    def aggregate_fit(
        self,
        server_round: int,
        results: list[tuple[ClientProxy, FitRes]],
        failures: list[Union[tuple[ClientProxy, FitRes], BaseException]],
    ) -> tuple[Optional[Parameters], dict[str, Scalar]]:
        """Aggregate the fit results from all clients."""
        parameters_aggregated, metrics_aggregated = super().aggregate_fit(server_round, results, failures)

        # Save aggregated model weights
        aggregated_ndarrays = parameters_to_ndarrays(parameters_aggregated)
        print("\n===  aggregated_ndarrays (round #{}):\n{}\n===\n".format(
            server_round,
            aggregated_ndarrays[0].flatten()[:30])
        )
        if is_saving(
            self.info_for_model_saving["saving_period"],
            server_round,
            self.info_for_model_saving["num_rounds"]
        ):
            print(f"Saving round #{server_round} aggregated_ndarrays...")
            num_clients = len(results) + len(failures)
            saving_file_name = "{}-{}-num-{}-seed-{}-lr-{}-round-{}-weights.npz".format(
                self.info_for_model_saving["dataset_name"],
                self.info_for_model_saving["model_name"],
                num_clients,
                self.info_for_model_saving.get("seed", "None"),
                self.info_for_model_saving["learning_rate"],
                server_round,
            )
            saving_file_path = os.path.join(self.info_for_model_saving["saving_folder"], saving_file_name)
            np.savez(saving_file_path, *aggregated_ndarrays)

        return parameters_aggregated, metrics_aggregated