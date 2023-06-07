#!/usr/bin/python3

for bet in range(122, 96, -1):
    if (bet % 2 != 0):
        bet = bet - 32
    print("{}".format(chr(bet)), end="")
