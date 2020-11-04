import numpy as np
import math

__main__ = ['softmax']

def softmax(x: list):
    """ applies softmax to an input x"""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis = 0)

def d_softmax(x):
    """This function is to calculate derivatives of relu of x"""
    return 1-(math.atan(x)*math.atan(x))
