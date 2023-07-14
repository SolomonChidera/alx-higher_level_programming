#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    a function that returns a new dictionary
    with all values multiplied by 2
    """
    multiply_dictionary = a_dictionary.copy()
    for k, v in multiply_dictionary.items():
        multiply_dictionary[k] = v * 2

    return multiply_dictionary
