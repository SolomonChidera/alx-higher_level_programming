#!/usr/bin/python3
"""
a function that divides element by element 2 lists
"""


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    div_elm = 0
    for i in range(list_length):
        try:
            div_elm = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div_elm = 0
        except ZeroDivisionError:
            print("division by 0")
            div_elm = 0
        except IndexError:
            print("out of range")
            div_elm = 0
        finally:
            new_list.append(div_elm)
    return new_list