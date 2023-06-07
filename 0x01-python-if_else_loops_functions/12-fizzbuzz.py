#!/usr/bin/python3
def fizzbuzz():
    for j in range(1, 101):
        if (j % 3 == 0 and j % 5 == 0):
            print("{}".format("FizzBuzz"), end=' ')
        elif (j % 3 == 0):
            print("{}".format("Fizz"), end=' ')
        elif (j % 5 == 0):
            print("{}".format("Buzz"), end=' ')
        else:
            print("{}".format(j), end=' ')
