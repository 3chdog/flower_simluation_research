"""pytorchexample: A Flower / PyTorch app."""

import os
import datetime
import numpy as np
from typing import List, Tuple

from flwr.common import Context, Metrics, ndarrays_to_parameters
from flwr.server import ServerApp, ServerAppComponents, ServerConfig

from pytorchexample.task import Net, get_weights, set_seed
from pytorchexample.strategy import FedAvgWithSaving, on_fit_config


# Define metric aggregation function
def weighted_average(metrics: List[Tuple[int, Metrics]]) -> Metrics:
    # Multiply accuracy of each client by number of examples used
    accuracies = [num_examples * m["accuracy"] for num_examples, m in metrics]
    examples = [num_examples for num_examples, _ in metrics]

    # Aggregate and return custom metric (weighted average)
    return {"accuracy": sum(accuracies) / sum(examples)}


def server_fn(context: Context):
    """Construct components that set the ServerApp behaviour."""

    # Read from config
    num_rounds = context.run_config["num-server-rounds"]
    seed = context.run_config.get("seed", None)

    # Prepare information for model saving
    info_for_model_saving = {
        "num_rounds": num_rounds,
        "model_name": context.run_config["model-name"],
        "dataset_name": context.run_config["dataset-name"],
        "seed": seed,
        "learning_rate": context.run_config["learning-rate"],
        "saving_folder": "./models/{}".format(datetime.datetime.now().strftime("%Y%m%d-%H%M%S")),
        "saving_period": context.run_config.get("saving-period", None),
    }
    if not os.path.exists(info_for_model_saving["saving_folder"]):
        os.makedirs(info_for_model_saving["saving_folder"])

    # Initialize model parameters
    if seed is None:
        print("Not set seed, run FL generally.")
    else:
        set_seed(seed)
    ndarrays = get_weights(Net())
    print("\n===  server initial parameters:\n{}\n===\n".format(ndarrays[0].flatten()[:30]))
    parameters = ndarrays_to_parameters(ndarrays)

    # save initial model weights
    print(f"Saving round #{0} aggregated_ndarrays...")
    saving_file_name = "{}-{}-num-{}-seed-{}-lr-{}-round-{}-weights.npz".format(
        info_for_model_saving["dataset_name"],
        info_for_model_saving["model_name"],
        "notyet",
        info_for_model_saving.get("seed", "None"),
        info_for_model_saving["learning_rate"],
        0,
    )
    saving_file_path = os.path.join(info_for_model_saving["saving_folder"], saving_file_name)
    np.savez(saving_file_path, *ndarrays)

    # Define the strategy
    strategy = FedAvgWithSaving(
        fraction_fit=1.0,
        fraction_evaluate=context.run_config["fraction-evaluate"],
        min_available_clients=2,
        evaluate_metrics_aggregation_fn=weighted_average,
        initial_parameters=parameters,
        on_fit_config_fn=on_fit_config, # send round number in "config" to clients
        info_for_model_saving=info_for_model_saving,
    )
    config = ServerConfig(num_rounds=num_rounds)

    return ServerAppComponents(strategy=strategy, config=config)


# Create ServerApp
app = ServerApp(server_fn=server_fn)
