#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return 0

    sum_n = 0
    roman_n = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    len_n = len(roman_string)
    for x in range(len_n):
        if roman_n.get(roman_string[x], 0) == 0:
            return 0

        if (x != (len_n - 1) and
                roman_n[roman_string[x]] < roman_n[roman_string[x + 1]]):
            sum_n += roman_n[roman_string[x]] * -1
        else:
            sum_n += roman_n[roman_string[x]]
    return sum_n
