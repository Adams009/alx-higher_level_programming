#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set()

    for num in my_list:
        new.add(num)

    addition = sum(new)

    return addition
