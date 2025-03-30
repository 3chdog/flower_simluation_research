"""pytorchexample: A Flower / PyTorch app."""

import torch
from flwr.client import ClientApp, NumPyClient
from flwr.common import Context

from pytorchexample.task import Net, get_weights, load_data, set_weights, test, train, OptimizerParameters

def get_optimizer_parameters_dict(run_config: dict) -> dict:
    optimizer_parameters = {}
    for k, v in run_config.items():
        if k.startswith("optimizer-"):
            dict_k = k.split("optimizer-")[1]
            optimizer_parameters[dict_k] = v
    return optimizer_parameters

# Define Flower Client
class FlowerClient(NumPyClient):
    def __init__(self, trainloader, valloader, local_epochs, optimizer_parameters, cid, rounds, seed):
        self.net = Net()
        self.trainloader = trainloader
        self.valloader = valloader
        self.local_epochs = local_epochs
        self.optimizer_parameters = optimizer_parameters
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.cid = cid
        self.rounds = rounds
        self.seed = seed

    def fit(self, parameters, config):
        """Train the model with data of this client."""
        set_weights(self.net, parameters)
        results = train(
            self.net,
            self.trainloader,
            self.valloader,
            self.local_epochs,
            self.optimizer_parameters,
            self.device,
            self.rounds,
            self.seed,
        )
        return get_weights(self.net), len(self.trainloader.dataset), results

    def evaluate(self, parameters, config):
        """Evaluate the model on the data this client has."""
        set_weights(self.net, parameters)
        loss, accuracy = test(self.net, self.valloader, self.device)
        return loss, len(self.valloader.dataset), {"accuracy": accuracy}


def client_fn(context: Context):
    """Construct a Client that will be run in a ClientApp."""

    # Read the node_config to fetch data partition associated to this node
    partition_id = context.node_config["partition-id"]
    num_partitions = context.node_config["num-partitions"] # options.num-supernodes
    rounds = context.run_config["num-server-rounds"]
    batch_size = context.run_config["batch-size"]
    local_epochs = context.run_config["local-epochs"]
    hetero = context.run_config.get("hetero")
    seed = context.run_config.get("seed", None)
    optimizer_parameters_dict = get_optimizer_parameters_dict(context.run_config)
    optimizer_parameters = OptimizerParameters(**optimizer_parameters_dict)

    # Read run_config to fetch hyperparameters relevant to this run
    trainloader, valloader = load_data(partition_id, num_partitions, batch_size, hetero, seed)

    # Return Client instance
    return FlowerClient(trainloader, valloader, local_epochs, optimizer_parameters, partition_id, rounds, seed).to_client()


# Flower ClientApp
app = ClientApp(client_fn)
