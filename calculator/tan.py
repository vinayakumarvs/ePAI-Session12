import math

__main__ = ['tan']

def tan(x, unit:'string'):
    '''
    This function is to calculate tan of x
    '''
    if unit == 'radian':
        return math.tan(math.degrees(x))
    else:
        return math.tan(x)


def d_tan(x, unit:'string'):
    '''
    This function is to calculate derivative of tan of x
    '''
    if unit == 'radian':
        return 1/ (math.cos(math.degrees(x)))**2
    else:
        return 1/(math.cos(x))**2
