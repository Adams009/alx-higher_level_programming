#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    maxi = my_list[0]

    for m in my_list:
        if m > maxi:
            maxi = m

    return maxi
