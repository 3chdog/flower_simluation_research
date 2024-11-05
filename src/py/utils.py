import torch
import torch.nn as nn
import torch.nn.functional as F

from torchvision.transforms import ToTensor, Normalize, Compose

DETERMINED_DATASET = "mnist" ### mnist or cifar10
BATCH_IMG_KEY = "img" if DETERMINED_DATASET == "cifar10" else "image"

# transformation to convert images to tensors and apply normalization
def apply_transforms(batch):
    transforms = Compose([ToTensor(), Normalize((0.1307,), (0.3081,))])
    batch[BATCH_IMG_KEY] = [transforms(img) for img in batch[BATCH_IMG_KEY]]
    return batch


# Model (simple CNN adapted from 'PyTorch: A 60 Minute Blitz')
# from torchvision.models.resnet import resnet50 as _resnet50

# class Net(nn.Module):
#     def __init__(self, num_classes=10):
#         super(Net, self).__init__()
#         self.model_resnet = _resnet50(weights=None)
#         num_ftrs = self.model_resnet.fc.in_features
#         self.model_resnet.fc = nn.Identity()
#         self.fc1 = nn.Linear(num_ftrs, num_classes)

#     def forward(self, x):
#         x = self.model_resnet(x)
#         out = self.fc1(x)
#         return out

if DETERMINED_DATASET=="cifar10":
    import resnet
    class Net(resnet.ResNet):
        def __init__(self, num_classes=10):
            super(Net, self).__init__(resnet.Bottleneck, [2,2,2,2], num_classes=num_classes)

else:
    class Net(nn.Module):
        def __init__(self, num_classes: int = 10) -> None:
            super(Net, self).__init__()
            self.conv1 = nn.Conv2d(1, 6, 5)
            self.pool = nn.MaxPool2d(2, 2)
            self.conv2 = nn.Conv2d(6, 16, 5)
            self.fc1 = nn.Linear(16 * 4 * 4, 120)
            self.fc2 = nn.Linear(120, 84)
            self.fc3 = nn.Linear(84, num_classes)

        def forward(self, x: torch.Tensor) -> torch.Tensor:
            x = self.pool(F.relu(self.conv1(x)))
            x = self.pool(F.relu(self.conv2(x)))
            x = x.view(-1, 16 * 4 * 4)
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = self.fc3(x)
            return x


# borrowed from Pytorch quickstart example
def train(net, trainloader, optim, epochs, device: str):
    """Train the network on the training set."""
    criterion = torch.nn.CrossEntropyLoss()
    net.train()
    for _ in range(epochs):
        for batch in trainloader:
            images, labels = batch[BATCH_IMG_KEY].to(device), batch["label"].to(device)
            optim.zero_grad()
            loss = criterion(net(images), labels)
            loss.backward()
            optim.step()


# borrowed from Pytorch quickstart example
def test(net, testloader, device: str):
    """Validate the network on the entire test set."""
    criterion = torch.nn.CrossEntropyLoss()
    correct, loss = 0, 0.0
    net.eval()
    with torch.no_grad():
        for data in testloader:
            images, labels = data[BATCH_IMG_KEY].to(device), data["label"].to(device)
            outputs = net(images)
            loss += criterion(outputs, labels).item()
            _, predicted = torch.max(outputs.data, 1)
            correct += (predicted == labels).sum().item()
    accuracy = correct / len(testloader.dataset)
    return loss, accuracy
