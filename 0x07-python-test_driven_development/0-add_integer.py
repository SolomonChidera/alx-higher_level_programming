#!/usr/bin/python3
"""
    Add two integers and return its sum
"""


def add_integer(a, b=98):
    """Adds 2 integers.
    Args:
        a (int): first number
        b (int): second number or 98 default
    Returns:
        Sum of the two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return (a + b)
