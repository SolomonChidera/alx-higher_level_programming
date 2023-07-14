#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    b = len(my_list)
    if idx >= b or idx < 0:
        return my_list
    for m in range(b):
        if m == idx:
            my_list[m] = element
    return my_list
