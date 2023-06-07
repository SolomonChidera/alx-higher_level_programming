#!/usr/bin/python3
for me in range(97, 123):
    if (me == 101 or me == 113):
        continue
    print("{}".format(chr(me)), end='')
