#!/usr/bin/python3
"""Define a integer adds function"""


def add_integer(a, b=98):

    """Return the integer adds of a and b
    
    Floats arguments are typecasted to  
    ints  before addition  is performed

    If the arguments are not integers,
      a TypeError exception is thrown
    """
    if ((not isinstance(a, int) and not
    isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not
    isinstance(b, float))):
        raise TypeError("b must be an integer")
    
    a = int(a)
    b = int(b)

    return a + b
