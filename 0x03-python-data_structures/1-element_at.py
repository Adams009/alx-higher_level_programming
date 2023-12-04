#!/usr/bin/python3
def element_at(my_list, idx):
    count = 0
    for i in my_list:
        count += 1
    return (my_list[idx] if 0 <= idx < count else None)
