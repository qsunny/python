# https://blog.csdn.net/qq_42283621/article/details/125052688

# 因为我们的模型只用到了CLIP视觉的编码器，所以我们只输出视觉编码器的参数有没有变化即可
# 不打开位置1和位置2，全部输出False，即所有参数都进行了更新
# 仅打开位置1，CLIP的参数为True，Linear为False，即Linear的参数更新
# 仅打开位置2，CLIP的参数为Flase，Linear为True，即只有CLIP的参数更新


import os
import clip
from torch import nn
from torch.utils.data import DataLoader
from torchvision.datasets import CIFAR10
from torch.nn import functional as F
import torch


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.model, self.preprocess = clip.load('ViT-B/32', 'cpu')
        self.linear = nn.Linear(512, 10)

        # 位置2
        # for param in self.linear.parameters():
        #    param.requires_grad = False

    def forward(self, x):
        features = self.model.encode_image(x)

        # 位置1
        # features = features.detach()

        return self.linear(features)


net = Net()
optimizer = torch.optim.SGD(net.parameters(), lr=1e-2)

root = os.path.expanduser("~/.cache")
train = CIFAR10(root, download=True, train=True, transform=net.preprocess)
train = next(iter(DataLoader(train, batch_size=8)))

storeParam = {}
for name, param in net.model.visual.named_parameters():
    storeParam[name] = param.detach().clone()
for name, param in net.linear.named_parameters():
    storeParam[name] = param.detach().clone()

for i in range(10):
    out = net(train[0])
    loss = F.cross_entropy(out, train[1])

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(loss.item())

for name, param in net.model.visual.named_parameters():
    print(f"{name} {torch.equal(param, storeParam[name])}")
for name, param in net.linear.named_parameters():
    print(f"{name} {torch.equal(param, storeParam[name])}")

