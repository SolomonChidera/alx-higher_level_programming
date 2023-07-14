#!/usr/bin/python3

def element_at(my_list, idx):
    if (idx < 0 and idx >= len(my_list)):
        return None
    for m in range(len(my_list)):
        if m == idx:
            return my_list[m]
