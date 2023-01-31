#!/usr/bin/python3
"""
4-print_square print a square using symbols
print_square(size) function printing the square
"""

def print_square(size):
    """
    >>> print_sqaure(5)
    #####
    #####
    #####
    #####
    #####
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        print("#" * size)
