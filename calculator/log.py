import numpy as np

__main__ = ['log']

def log(x):
    """This function is to calculate natural Logarithm of x with base e
    """
    return np.log(x)

def d_log(x):
    """This function is to calculate Derivative of natural Logarithm of x 
    """
    return 1/x
