#!/usr/bin/python3

if __name__ == "__main__":

    """Prints the results of the addition of all arguments"""

    import sys

    num = len(sys.argv) - 1
    count = 0

    if (num == 0):
        print(0)
    else:
        for i in range(num):
            count += int(sys.argv[i + 1])
        print(count)
