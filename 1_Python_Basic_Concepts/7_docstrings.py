'''
Python Comments vs Docstrings
1. Python Comments are descriptions that help programmers better understand the intent and functionality of the program. 
They are completely ignored by the Python interpreter.

2. Python docstrings are strings literals used right after the definition of a function, method, class, or module.
They are used to document our code.  They are associated with the object as their doc attribute thus we can
access these docstrings using the doc attribute.
'''


def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2


print(square.__doc__)