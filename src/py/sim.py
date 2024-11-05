import argparse
from collections import OrderedDict
from typing import Dict, Tuple, List

import torch
from torch.utils.data import DataLoader

import flwr as fl
from flwr.common import Metrics
from flwr.common.typing import Scalar

from datasets import Dataset
from datasets.utils.logging import disable_progress_bar
from flwr_datasets import FederatedDataset

from utils import Net, train, test, apply_transforms

###==time
import time
time_collect = True
if time_collect: from flwr.common.orchid_logger import flwrsim_logger; from flwr.common.constant import MessageType
###==

parser = argparse.ArgumentParser(description="Flower Simulation with PyTorch")

parser.add_argument(
    "--num_cpus",
    type=int,
    default=4,
    help="Number of CPUs to assign to a virtual client",
)
parser.add_argument(
    "--num_gpus",
    type=float,
    default=1.0,
    help="Ratio of GPU memory to assign to a virtual client",
)

DETERMINED_DATASET = "mnist" ### mnist or cifar10

NUM_CLIENTS = 10
NUM_ROUNDS = 20
SELECTED_RATIO = 1.0

# Flower client, adapted from Pytorch quickstart example
class FlowerClient(fl.client.NumPyClient):
    def __init__(self, trainset, valset, msg_type, cid, roundNum):
        ###==time
        if time_collect: flwrsim_logger.info("event: {0} | time: {1}".format("FlowerClient __init__() start {}; cid ==={}=== round #{}".format(msg_type, cid, roundNum), time.time()))
        ###==
        self.trainset = trainset
        self.valset = valset

        ###==time
        if time_collect: flwrsim_logger.info("event: {0} | time: {1}".format("FlowerClient __init__() / self.model = Net() {}; cid ==={}=== round #{}".format(msg_type, cid, roundNum), time.time()))
        ###==
        # Instantiate model
        self.model = Net()
        ###==time
        if time_collect: flwrsim_logger.info("event: {0} | time: {1}".format("FlowerClient __init__() done Net() {}; cid ==={}=== round #{}".format(msg_type, cid, roundNum), time.time()))
        ###==

        # Determine device
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)  # send model to device
        ###==time
        if time_collect: flwrsim_logger.info("event: {0} | time: {1}".format("FlowerClient __init__() END {}; cid ==={}=== round #{}".format(msg_type, cid, roundNum), time.time()))
        ###==

    def get_parameters(self, config):
        return [val.cpu().numpy() for _, val in self.model.state_dict().items()]

    def fit(self, parameters, config):
        ###==time
        print("FlowerClient train:\n", config)
        fit_time_collect = True
        cid = None
        roundNum = None
        if "cid" not in config.keys() or "roundNum" not in config.keys():
            print("\n\nRUNNING sim.py/FlowerClient.fit()\nlack of \"cid\" or \"roundNum\" in config. no logging.\n\n")
            fit_time_collect = False
        else:
            cid = config["cid"]
            roundNum = config["roundNum"]
        ###==
        ###==time
        if time_collect and fit_time_collect: flwrsim_logger.info("event: {0} | time: {1}".format("into client.func() / gonna set_params() {}; cid ==={}=== round #{}".format(MessageType.TRAIN, cid, roundNum), time.time()))
        ###==
        set_params(self.model, parameters)
        ###==time
        if time_collect and fit_time_collect: flwrsim_logger.info("event: {0} | time: {1}".format("done set_params() / gonna set DataLoader(not create dataset) {}; cid ==={}=== round #{}".format(MessageType.TRAIN, cid, roundNum), time.time()))
        ###==

        # Read from config
        batch, epochs = config["batch_size"], config["epochs"]

        # Construct dataloader
        trainloader = DataLoader(self.trainset, batch_size=batch, shuffle=True)
        ###==time
        if time_collect and fit_time_collect: flwrsim_logger.info("event: {0} | time: {1}".format("done set DataLoader(not create dataset) / gonna set optimizer {}; cid ==={}=== round #{}".format(MessageType.TRAIN, cid, roundNum), time.time()))
        ###==

        # Define optimizer
        optimizer = torch.optim.SGD(self.model.parameters(), lr=0.01, momentum=0.9)
        ###==time
        if time_collect and fit_time_collect: flwrsim_logger.info("event: {0} | time: {1}".format("done set optimizer / gonna train()/test() epochs {}; cid ==={}=== round #{}".format(MessageType.TRAIN, cid, roundNum), time.time()))
        ###==
        # Train
        train(self.model, trainloader, optimizer, epochs=epochs, device=self.device)
        ###==time
        if time_collect and fit_time_collect: flwrsim_logger.info("event: {0} | time: {1}".format("done train()/test() epochs / gonna return to ray_client_proxy {}; cid ==={}=== round #{}".format(MessageType.TRAIN, cid, roundNum), time.time()))
        ###==

        # Return local model and statistics
        return self.get_parameters({}), len(trainloader.dataset), {}

    def evaluate(self, parameters, config):
        ###==time
        print("FlowerClient eval:\n", config)
        eval_time_collect = True
        cid = None
        roundNum = None
        if "cid" not in config.keys() or "roundNum" not in config.keys():
            print("RUNNING sim.py/FlowerClient.evaluate()\nlack of \"cid\" or \"roundNum\" in config. no logging.\n\n")
            eval_time_collect = False
        else:
            cid = config["cid"]
            roundNum = config["roundNum"]
        ###==
        ###==time
        if time_collect and eval_time_collect: flwrsim_logger.info("event: {0} | time: {1}".format("into client.func() / gonna set_params() {}; cid ==={}=== round #{}".format(MessageType.EVALUATE, cid, roundNum), time.time()))
        ###==
        set_params(self.model, parameters)
        ###==time
        if time_collect and eval_time_collect: flwrsim_logger.info("event: {0} | time: {1}".format("done set_params() / gonna set DataLoader(not create dataset) {}; cid ==={}=== round #{}".format(MessageType.EVALUATE, cid, roundNum), time.time()))
        ###==

        # Construct dataloader
        valloader = DataLoader(self.valset, batch_size=64)
        ###==time
        if time_collect and eval_time_collect: flwrsim_logger.info("event: {0} | time: {1}".format("done set DataLoader(not create dataset) / gonna set optimizer {}; cid ==={}=== round #{}".format(MessageType.EVALUATE, cid, roundNum), time.time()))
        ###==
        ###==time
        if time_collect and eval_time_collect: flwrsim_logger.info("event: {0} | time: {1}".format("done set optimizer / gonna train()/test() epochs {}; cid ==={}=== round #{}".format(MessageType.EVALUATE, cid, roundNum), time.time()))
        ###==

        # Evaluate
        loss, accuracy = test(self.model, valloader, device=self.device)
        ###==time
        if time_collect and eval_time_collect: flwrsim_logger.info("event: {0} | time: {1}".format("done train()/test() epochs / gonna return to ray_client_proxy {}; cid ==={}=== round #{}".format(MessageType.EVALUATE, cid, roundNum), time.time()))
        ###==

        # Return statistics
        return float(loss), len(valloader.dataset), {"accuracy": float(accuracy)}


def get_client_fn(dataset: FederatedDataset):
    """Return a function to construct a client.

    The VirtualClientEngine will execute this function whenever a client is sampled by
    the strategy to participate.
    """

    def client_fn(cid: str) -> fl.client.Client:
        """Construct a FlowerClient with its own dataset partition."""
        msg_type, cid, roundNum = cid.split("!!!")
        ###==time
        if time_collect: flwrsim_logger.info("event: {0} | time: {1}".format("ray_client_fn start {}; cid ==={}=== round #{}".format(msg_type, cid, roundNum), time.time()))
        ###==

        # Let's get the partition corresponding to the i-th client
        client_dataset = dataset.load_partition(int(cid), "train")
        ###==time
        if time_collect: flwrsim_logger.info("event: {0} | time: {1}".format("done load_partition / split and transform dataset {}; cid ==={}=== round #{}".format(msg_type, cid, roundNum), time.time()))
        ###==

        # Now let's split it into train (90%) and validation (10%)
        client_dataset_splits = client_dataset.train_test_split(test_size=0.1, seed=45)

        trainset = client_dataset_splits["train"]
        valset = client_dataset_splits["test"]

        # Now we apply the transform to each batch.
        trainset = trainset.with_transform(apply_transforms)
        valset = valset.with_transform(apply_transforms)
        ###==time
        if time_collect: flwrsim_logger.info("event: {0} | time: {1}".format("done split and transform dataset / call FlowerClient {}; cid ==={}=== round #{}".format(msg_type, cid, roundNum), time.time()))
        ###==

        # Create and return client
        return FlowerClient(trainset, valset, msg_type, cid, roundNum).to_client()

    return client_fn


def fit_config(server_round: int) -> Dict[str, Scalar]:
    """Return a configuration with static batch size and (local) epochs."""
    config = {
        "epochs": 1,  # Number of local epochs done by clients
        "batch_size": 64,  # Batch size to use by clients during fit()
    }
    return config


def set_params(model: torch.nn.ModuleList, params: List[fl.common.NDArrays]):
    """Set model weights from a list of NumPy ndarrays."""
    params_dict = zip(model.state_dict().keys(), params)
    state_dict = OrderedDict({k: torch.Tensor(v) for k, v in params_dict})
    for k in list(state_dict.keys()):
        if "num_batches_tracked" in k:
            del state_dict[k]
    model.load_state_dict(state_dict, strict=True)


def weighted_average(metrics: List[Tuple[int, Metrics]]) -> Metrics:
    """Aggregation function for (federated) evaluation metrics, i.e. those returned by
    the client's evaluate() method."""
    # Multiply accuracy of each client by number of examples used
    accuracies = [num_examples * m["accuracy"] for num_examples, m in metrics]
    examples = [num_examples for num_examples, _ in metrics]

    # Aggregate and return custom metric (weighted average)
    return {"accuracy": sum(accuracies) / sum(examples)}


def get_evaluate_fn(
    centralized_testset: Dataset,
):
    """Return an evaluation function for centralized evaluation."""

    def evaluate(
        server_round: int, parameters: fl.common.NDArrays, config: Dict[str, Scalar]
    ):
        """Use the entire CIFAR-10 test set for evaluation."""

        # Determine device
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

        model = Net()
        set_params(model, parameters)
        model.to(device)

        # Apply transform to dataset
        testset = centralized_testset.with_transform(apply_transforms)

        # Disable tqdm for dataset preprocessing
        disable_progress_bar()

        testloader = DataLoader(testset, batch_size=50)
        loss, accuracy = test(model, testloader, device=device)

        return loss, {"accuracy": accuracy}

    return evaluate


# Download MNIST dataset and partition it
mnist_fds = FederatedDataset(dataset=DETERMINED_DATASET, partitioners={"train": NUM_CLIENTS})
centralized_testset = mnist_fds.load_split("test")

# Configure the strategy
strategy = fl.server.strategy.FedAvg(
    fraction_fit=SELECTED_RATIO,  # Sample 10% of available clients for training
    fraction_evaluate=0.05,  # Sample 5% of available clients for evaluation
    min_available_clients=int(NUM_CLIENTS*SELECTED_RATIO),
    on_fit_config_fn=fit_config,
    evaluate_metrics_aggregation_fn=weighted_average,  # Aggregate federated metrics
    evaluate_fn=get_evaluate_fn(centralized_testset),  # Global evaluation function
)

# ClientApp for Flower-Next
client = fl.client.ClientApp(
    client_fn=get_client_fn(mnist_fds),
)

# ServerApp for Flower-Next
server = fl.server.ServerApp(
    config=fl.server.ServerConfig(num_rounds=NUM_ROUNDS),
    strategy=strategy,
)


def main():
    ###==time
    if time_collect: flwrsim_logger.info("event: {0} | time: {1}".format("start run_sim", time.time()))
    ###==
    # Parse input arguments
    args = parser.parse_args()

    # Resources to be assigned to each virtual client
    client_resources = {
        "num_cpus": args.num_cpus,
        "num_gpus": args.num_gpus,
    }

    # Start simulation
    # print("\n=*=*=*\n{}: {}\n=*=*=*\n".format("init start", time.time()))
    fl.simulation.start_simulation(
        client_fn=get_client_fn(mnist_fds),
        num_clients=NUM_CLIENTS,
        client_resources=client_resources,
        config=fl.server.ServerConfig(num_rounds=NUM_ROUNDS),
        strategy=strategy,
        actor_kwargs={
            "on_actor_init_fn": disable_progress_bar  # disable tqdm on each actor/process spawning virtual clients
        },
    )
    ###==time
    if time_collect: flwrsim_logger.info("event: {0} | time: {1}".format("END run_sim", time.time()))
    ###==


if __name__ == "__main__":
    main()
