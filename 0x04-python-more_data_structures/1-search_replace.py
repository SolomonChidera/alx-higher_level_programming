#!/usr/bin/python3

def search_replace(my_list, search, replace):

    """
    a function that replaces all occurrences
    of an element by another in a new list.
    """
    list_len = len(my_list)
    new_list = my_list.copy()

    for idx in range(list_len):
        if new_list[idx] == search:
            new_list[idx] = replace

    return new_list
