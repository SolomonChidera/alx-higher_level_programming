#!/usr/bin/python3

def best_score(a_dictionary):
    """
    a function that returns a key
    with the biggest integer value.
    """
    if not a_dictionary:
        return None
    max_value = max(a_dictionary, key=a_dictionary.get)
    return max_value
