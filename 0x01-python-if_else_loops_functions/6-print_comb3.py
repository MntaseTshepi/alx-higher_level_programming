#!/usr/bin/python3

for val in range(0, 10):
    for val2 in range(val+1, 10):
        if val != val2:
            if val == 8 and val2 == 9:
                print("{}{}".format(val, val2))
            else:
                print("{}{}".format(val, val2), end=", ")
