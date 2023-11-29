#!/usr/bin/python3
def fizzbuzz():
    for ite in range(1, 101):
        if (ite % 3 == 0 and ite % 5 != 0):
            print("Fizz ", end='')
        elif (ite % 5 == 0 and ite % 3 != 0):
            print("Buzz ", end='')
        elif (ite % 5 == 0 and ite % 3 == 0):
            print("FizzBuzz ", end='')
        else:
            print("{} ".format(ite), end='')
