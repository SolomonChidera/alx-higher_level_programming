#!/usr/bin/python3
for number in range(0, 100):
    if number == 99:
        print("{0:d}".format(number))
        continue
    print("{0:02}".format(number), end=', ')
