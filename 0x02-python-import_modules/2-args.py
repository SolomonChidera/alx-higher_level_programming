#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    args = len(argv)
    num = 1

    if (args == 1):
        print("{} arguments.".format(args - 1))
    elif (args > 1):
        i = '' if args == 2 else 'i'
        print("{} argument{}:".format(args - 1, i))

    while num < args:
        print("{}: {}".format(num, argv[num]))
        num += 1
