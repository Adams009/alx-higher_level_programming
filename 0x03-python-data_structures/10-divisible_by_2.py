#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return []

    new_list = [d % 2 == 0 for d in my_list]

    return new_list
