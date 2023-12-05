#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return []

    for d in my_list:
        new_list = [d % 2 == 0]

    return new_list
