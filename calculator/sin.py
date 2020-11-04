import math

__main__ = ['sin']

def sin(x, unit:'string'):
    '''
    This function is to calculate sin of x
    '''
    if unit == 'radian':
        return math.sin(math.degrees(x))
    else:
        return math.sin(x)

def d_sin(x, unit:'string'):
    '''
    This function is to calculate derivative of sin(x)
    '''
    if unit == 'radian':
        return math.cos(math.degrees(x))
    else:
        return math.cos(x)
