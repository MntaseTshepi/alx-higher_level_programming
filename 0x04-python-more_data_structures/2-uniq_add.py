#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds unique numbers together"""

    uniq_list = []
    sum_of = 0

    for i in my_list:
        if i in uniq_list:
            continue
        else:
            uniq_list.append(i)

    for i in uniq_list:
        sum_of += i

    return(sum_of)
