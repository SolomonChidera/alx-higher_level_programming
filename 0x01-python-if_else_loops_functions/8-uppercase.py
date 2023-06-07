#!/usr/bin/python3
def uppercase(str):
    for me in str:
        if (ord(me) >= 97 and ord(me) <= 122):
            me = chr(ord(me) - 32)
        print("{}".format(me), end='')
    print()
