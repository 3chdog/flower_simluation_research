"""pytorchexample: A Flower / PyTorch app."""

import torch
from flwr.client import ClientApp, NumPyClient
from flwr.common import Context

from pytorchexample.task import Net, get_weights, load_data, set_weights, test, train

def get_optim_params(run_config: dict):
    optim_params = {}
    for k, v in run_config.items():
        if k.startswith("optim-"):
            optim_params[k] = v
    return optim_params

# Define Flower Client
class FlowerClient(NumPyClient):
    def __init__(self, trainloader, valloader, local_epochs, optim_params, cid, rounds, seed):
        self.net = Net()
        self.trainloader = trainloader
        self.valloader = valloader
        self.local_epochs = local_epochs
        self.optim_params = optim_params
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.cid = cid
        self.rounds = rounds
        self.seed = seed

    def fit(self, parameters, config):
        # print("\n===  config\n{}\n===\n".format(config))
        # print("\n===  parameters:\n{}\n===\n".format(parameters[0].flatten()[:30]))
        """Train the model with data of this client."""
        set_weights(self.net, parameters)
        results = train(
            self.net,
            self.trainloader,
            self.valloader,
            self.local_epochs,
            self.optim_params,
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
    num_partitions = context.node_config["num-partitions"]

    # Read run_config to fetch hyperparameters relevant to this run
    seed = context.run_config.get("seed", None)
    batch_size = context.run_config["batch-size"]
    trainloader, valloader = load_data(partition_id, num_partitions, batch_size, seed)
    local_epochs = context.run_config["local-epochs"]
    optim_params = get_optim_params(context.run_config)

    # server_rounds for generating seeds for epochs
    rounds = context.run_config["num-server-rounds"]

    # Return Client instance
    return FlowerClient(trainloader, valloader, local_epochs, optim_params, partition_id, rounds, seed).to_client()


# Flower ClientApp
app = ClientApp(client_fn)
