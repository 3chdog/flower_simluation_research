from typing import Optional, Union
from flwr.common import (
    FitRes,
    Parameters,
    Scalar,
    parameters_to_ndarrays
)
from flwr.server.client_proxy import ClientProxy
from flwr.server.strategy import FedAvg

class FedAvgWithSaving(FedAvg):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def aggregate_fit(
        self,
        server_round: int,
        results: list[tuple[ClientProxy, FitRes]],
        failures: list[Union[tuple[ClientProxy, FitRes], BaseException]],
    ) -> tuple[Optional[Parameters], dict[str, Scalar]]:
        """Aggregate the fit results from all clients."""
        parameters_aggregated, metrics_aggregated = super().aggregate_fit(server_round, results, failures)

        aggregated_ndarrays = parameters_to_ndarrays(parameters_aggregated)
        print("\n===  aggregated_ndarrays (round #{}):\n{}\n===\n".format(
            server_round,
            aggregated_ndarrays[0].flatten()[:30])
        )

        return parameters_aggregated, metrics_aggregated