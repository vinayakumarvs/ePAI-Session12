import numpy as np

__main__ = ['relu']

def relu(x):
    """This function is to calculate relu of x"""
    return np.maximum(0,x)

def d_relu(x):
    """This function is to calculate derivatives of relu of x"""
    if x > 0:
        return 1
    return 0
