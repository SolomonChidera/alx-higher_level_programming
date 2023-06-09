#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    sum_all = 0
    args = len(sys.argv)

    for j in range(1, args):
        sum_all += int(sys.argv[j])

    print("{:d}".format(sum_all))
