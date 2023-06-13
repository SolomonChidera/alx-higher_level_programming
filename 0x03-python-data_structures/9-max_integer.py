#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        my_list.sort()
        max_v = my_list.pop()
        return max_v
