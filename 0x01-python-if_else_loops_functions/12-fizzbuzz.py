#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if (number % 3 == 0 and number % 5 == 0):
            print("{}".format("FizzBuzz"), end=' ')
        elif (number % 3 == 0):
            print("{}".format("Fizz"), end=' ')
        elif (number % 5 == 0):
            print("{}".format("Buzz"), end=' ')
        else:
            print("{}".format(number), end=' ')
