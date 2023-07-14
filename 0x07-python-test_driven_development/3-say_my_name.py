#!/usr/bin/python3

"""
Prints a string that include the names passed
"""


def say_my_name(first_name, last_name=""):
    """Prints the format My name is <first name> <last name>

    Args:
        first_name (string): first name
        last_name (string): last name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
