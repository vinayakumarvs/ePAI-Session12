import math

__main__ = ['sigmoid']

def sigmoid(x):
    """The function will return sigmoid value"""
    return 1 / (1 + math.exp(-x))


def d_sigmoid(x):
    """The function will return Derivative of sigmoid value"""
    return (1 / (1 + math.exp(-x))) * (1-(1 / (1 + math.exp(-x))))
