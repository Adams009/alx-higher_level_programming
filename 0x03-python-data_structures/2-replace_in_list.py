#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    count = 0
    for i in my_list:
        count += 1
    if 0 <= idx < count:
        my_list[idx] = element
        return my_list
    else:
        return my_list
