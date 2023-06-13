#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx >= len(my_list) or idx < 0):
        return my_list
    new = my_list[:]
    new[idx] = element
    return new
