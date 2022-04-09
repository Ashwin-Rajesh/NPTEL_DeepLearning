#!~/anaconda3/bin/python3.8

import torch
import torch.nn.functional as F
from torch import nn
import numpy as np

def conv_out_size(size, kernel_size = 5, stride = 1, padding = 0):
    return (size - kernel_size + (2 * padding)) // stride

class QNetwork(nn.Module):
    def __init__(self, in_h, in_w, out):
        super(QNetwork, self).__init__()

        self.conv1 = nn.Conv2d(3, 16, kernel_size=5, stride=1)
        self.bn1   = nn.BatchNorm2d(16)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=5, stride=1)
        self.conv3 = nn.Conv2d(32, 32, kernel_size=5, stride=1)

        hidden_h = conv_out_size(conv_out_size(conv_out_size(h)))
        hidden_w = conv_out_size(conv_out_size(conv_out_size(w)))
        self.linear = nn.Linear(hidden_h*hidden_w, out)

    def forward(self, input):
        x = F.relu(self.bn1(self.conv1(input)))
        x = F.relu(self.bn2(self.conv2(x)))
        x = F.relu(self.bn3(self.conv3(x)))
        return F.softmax(self.linear(x.flatten()))

