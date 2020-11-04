import math

__main__ = ['tanh']
def tanh(x, unit:'string'):
    '''
    This function is to calculate hyperbolic tan of x
    '''
    if unit == 'radian':
        return math.tanh(math.degrees(x))
    else:
        return math.tanh(x)

def d_tanh(x, unit:'string'):
    '''
    This function is to calculate derivative of hyperbolic tan of x
    '''
    if unit == 'radian':
        return 1-(math.tanh(math.degrees(x)))**2
    else:
        return 1-(math.tanh(x))**2
