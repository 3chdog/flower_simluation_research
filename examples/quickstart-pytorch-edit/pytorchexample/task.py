"""pytorchexample: A Flower / PyTorch app."""

from collections import OrderedDict
from dataclasses import dataclass

import torch
import torch.nn as nn
import torch.nn.functional as F
from flwr_datasets import FederatedDataset
from flwr_datasets.partitioner import IidPartitioner, DirichletPartitioner
from torch.utils.data import DataLoader
from torchvision.transforms import Compose, Normalize, ToTensor

import random
import numpy as np

go_check_weights = True

@dataclass
class OptimizerParameters:
    name: str = "SGD" # flower expamle default
    learning_rate: float = 0.1 # flower expamle default
    momentum: float = 0.9 # flower expamle default
    weight_decay: float = 0 # torch default

def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)  # 用於多 GPU 訓練
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False  # 可能會降低性能，但可確保結果一致

def generate_seeds_for_epochs(num_random_numbers: int, seed:int):
    np.random.seed(seed)
    return np.random.randint(0, 2**32 - 1, size=round(num_random_numbers*1.5)).tolist()

class Net(nn.Module):
    """Model (simple CNN adapted from 'PyTorch: A 60 Minute Blitz')"""

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return self.fc3(x)


def get_weights(net):
    return [val.cpu().numpy() for _, val in net.state_dict().items()]


def set_weights(net, parameters):
    params_dict = zip(net.state_dict().keys(), parameters)
    state_dict = OrderedDict({k: torch.tensor(v) for k, v in params_dict})
    net.load_state_dict(state_dict, strict=True)


fds = None  # Cache FederatedDataset


def load_data(partition_id: int, num_partitions: int, batch_size: int, hetero: int = 0, seed: int = None):
    """Load partition CIFAR10 data."""
    # Only initialize `FederatedDataset` once
    if seed is None:
        seed = 42
    global fds
    if fds is None:
        if hetero:
            partitioner = DirichletPartitioner(
                num_partitions=num_partitions,
                partition_by="label",
                alpha=0.5,
                min_partition_size=10,
                self_balancing=True,
            )
        else:
            partitioner = IidPartitioner(num_partitions=num_partitions)
        fds = FederatedDataset(
            dataset="uoft-cs/cifar10",
            partitioners={"train": partitioner},
        )
    partition = fds.load_partition(partition_id)
    # Divide data on each node: 80% train, 20% test
    partition_train_test = partition.train_test_split(test_size=0.2, seed=seed)
    pytorch_transforms = Compose(
        [ToTensor(), Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
    )

    def apply_transforms(batch):
        """Apply transforms to the partition from FederatedDataset."""
        batch["img"] = [pytorch_transforms(img) for img in batch["img"]]
        return batch

    partition_train_test = partition_train_test.with_transform(apply_transforms)
    trainloader = DataLoader(
        partition_train_test["train"], batch_size=batch_size, shuffle=True
    )
    testloader = DataLoader(partition_train_test["test"], batch_size=batch_size)
    return trainloader, testloader


def get_optimizer(net, optimizer_parameters: OptimizerParameters):
    """Get optimizer based on the parameters."""
    if optimizer_parameters.name == "SGD":
        return torch.optim.SGD(
            net.parameters(),
            lr=optimizer_parameters.learning_rate,
            momentum=optimizer_parameters.momentum,
            weight_decay=optimizer_parameters.weight_decay,
        )
    elif optimizer_parameters.name == "Adam":
        return torch.optim.Adam(
            net.parameters(),
            lr=optimizer_parameters.learning_rate,
            weight_decay=optimizer_parameters.weight_decay,
        )
    else:
        raise ValueError(f"Unsupported optimizer: {optimizer_parameters.name}")

def train(net, trainloader, valloader, epochs, optimizer_parameters: OptimizerParameters, device, rounds, seed=None):
    """Train the model on the training set."""

    ###   seed section   ###
    if seed is not None:
        set_seed(seed)
        seeds_for_epochs = generate_seeds_for_epochs(epochs*rounds, seed)
    ### end seed section ###

    net.to(device)  # move model to GPU if available
    criterion = torch.nn.CrossEntropyLoss().to(device)
    optimizer = get_optimizer(net, optimizer_parameters)
    net.train()
    for epoch in range(epochs):
        ###   seed section   ###
        # set seed for trainloader to ensure the same seed sequence for each epoch
        if seed is not None:
            seed_for_this_epoch = seeds_for_epochs[((rounds-1) * epochs + epoch) % len(seeds_for_epochs)]
            set_seed(seed_for_this_epoch)
        ### end seed section ###
        for batch in trainloader:
            images = batch["img"]
            labels = batch["label"]
            optimizer.zero_grad()
            criterion(net(images.to(device)), labels.to(device)).backward()
            optimizer.step()

    val_loss, val_acc = test(net, valloader, device)

    results = {
        "val_loss": val_loss,
        "val_accuracy": val_acc,
    }
    return results


def test(net, testloader, device):
    """Validate the model on the test set."""
    net.to(device)  # move model to GPU if available
    criterion = torch.nn.CrossEntropyLoss()
    correct, loss = 0, 0.0
    with torch.no_grad():
        for batch in testloader:
            images = batch["img"].to(device)
            labels = batch["label"].to(device)
            outputs = net(images)
            loss += criterion(outputs, labels).item()
            correct += (torch.max(outputs.data, 1)[1] == labels).sum().item()
    accuracy = correct / len(testloader.dataset)
    loss = loss / len(testloader)
    return loss, accuracy
