#!/usr/bin/python3
"""
a function that divides 2 integers
and prints the result.
"""


def safe_print_division(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {}".format(res))
        return res
