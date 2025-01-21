import numpy as np 

def add(x, y):
    """Add two numbers or arrays.
    
    Parameters
    ----------
    x : int or float or array_like
        The first number to add.
    y : int or float or array_like
        The second number to add.
    
    Returns
    -------
    int or float or array_like
    The sum of x and y.
    """
    return x + y 

def multiply(x, y):
    """Multiply two numbers or arrays.
    
    Parameters
    ----------
    x : int or float or array_like
        The first number to multiply.
    y : int or float or array_like
        The second number to multiply.
    
    Returns
    -------
    int or float or array_like
    The (element-wise) product of x and y.
    """
    return x * y  

def divide(x, y):
    """Divide two numbers or arrays.
    
    Parameters
    ----------
    x : int or float or array_like
        The first number to divide.
    y : int or float or array_like
        The second number to divide.
    
    Returns
    -------
    int or float or array_like
    The quotient of x and y.
    """
    return x / y

def subtract(x, y):
    """Add two numbers or arrays.
    
    Parameters
    ----------
    x : int or float or array_like
        The first number to subract.
    y : int or float or array_like
        The second number to subtract.
    
    Returns
    -------
    int or float or array_like
    The difference of x and y.
    """
    return x - y

def modulo(x, y):
    """Returns the remainder of x divided by y.

    Parameters
    ----------
    x : int or float or array_like
        The first number to divide.
    y : int or float or array_like
        The second number to divide.

    Returns
    -------
    int or float or array_like
    The remainder of x divided by y.
    """
    return x % y == 0