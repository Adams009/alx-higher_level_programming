#!/usr/bin/python3
def remove_char_at(str, n):
    present = ''
    ite = 0
    for charac in str:
        if ite != n:
            present += str[ite]
        ite += 1
    return (present)
