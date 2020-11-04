import math

__all__ = ['cos']

def cos(x, unit:'string'):
    '''
    This function is to calculate Cosine(x)
    '''
    if unit == 'radian':
        return math.cos(math.degrees(x))
    else:
        return math.cos(x)

def d_cos(x, unit:'string'):
    '''
    This function is to calculate a derivative of Cosine(x)
    '''
    if unit == 'radian':
        return -math.sin(math.degrees(x))
    else:
        return -math.sin(x)
