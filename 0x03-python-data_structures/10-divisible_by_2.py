#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new = []
    for m in my_list:
        a = m % 2 == 0
        if a:
            new.append(True)
        else:
            new.append(False)
    return new
