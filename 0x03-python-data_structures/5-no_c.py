#!/usr/bin/python3

def no_c(my_string):
    """
    returns a new list
    """
    new_list = [n for n in my_string if n != "C" and n != "c"]
    return ("".join(new_list))
