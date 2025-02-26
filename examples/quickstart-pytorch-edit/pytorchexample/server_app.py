"""pytorchexample: A Flower / PyTorch app."""

from typing import List, Tuple

from flwr.common import Context, Metrics, ndarrays_to_parameters
from flwr.server import ServerApp, ServerAppComponents, ServerConfig
from flwr.server.strategy import FedAvg

from pytorchexample.task import Net, get_weights
from pytorchexample.strategy import CustomFedAvg

# Define metric aggregation function
def weighted_average(metrics: List[Tuple[int, Metrics]]) -> Metrics:
    # Multiply accuracy of each client by number of examples used
    accuracies = [num_examples * m["accuracy"] for num_examples, m in metrics]
    examples = [num_examples for num_examples, _ in metrics]

    # Aggregate and return custom metric (weighted average)
    return {"accuracy": sum(accuracies) / sum(examples)}


def get_model(dataset_model_type: str):
    if dataset_model_type == "mnist":
        return Net()
    elif dataset_model_type == "cifar10":
        from pytorchexample.task import resnet50_for_cifar10
        return resnet50_for_cifar10
    elif dataset_model_type == "cifar10_lenet":
        return Net()
    else:
        raise ValueError("Invalid dataset_model_type")

def server_fn(context: Context):
    """Construct components that set the ServerApp behaviour."""
    print("server_fn", context)

    # Read from config
    num_rounds = context.run_config["num-server-rounds"]

    # Initialize model parameters
    model = get_model(context.run_config["dataset_model_type"])
    ndarrays = get_weights(model)
    parameters = ndarrays_to_parameters(ndarrays)

    # Define the strategy
    strategy = FedAvg(
        fraction_fit=1.0,
        fraction_evaluate=context.run_config["fraction-evaluate"],
        min_available_clients=2,
        evaluate_metrics_aggregation_fn=weighted_average,
        initial_parameters=parameters,
    )
    config = ServerConfig(num_rounds=num_rounds)

    return ServerAppComponents(strategy=strategy, config=config)


# Create ServerApp
app = ServerApp(server_fn=server_fn)
