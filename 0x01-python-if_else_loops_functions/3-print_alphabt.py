#!/usr/bin/python3

#Prints the alphabet except q and e, not followed by new line.
for i in range(97, 123):
    if chr(i) == 'q' or chr(i) == 'e':
        continue
    print(f"{chr(i):s}", end="")
