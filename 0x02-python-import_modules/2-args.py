#!/usr/bin/python3

if __name__ == "__main__":

    """Prints the number of arguments and list of arguments"""

    import sys

    num = len(sys.argv) - 1

    if (num == 0):
        print("0 arguments.")
    elif (num == 1):
        print("1 argument:")
    else:
        print("{:d} arguments:".format(num))
    for i in range(num):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
