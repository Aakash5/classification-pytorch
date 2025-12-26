import torch

def basic_ops():
    x = torch.tensor([[1, 2], [3, 4]])
    y = x + 2
    return x, y
