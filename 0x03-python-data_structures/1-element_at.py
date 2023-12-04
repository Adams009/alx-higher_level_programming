#!/usr/bin/python3
def element_at(my_list, idx):
    count = 0
    for i in my_list:
        count += 1
    if 0 <= idx < count:
        return my_list[idx]
    else:
        return None
