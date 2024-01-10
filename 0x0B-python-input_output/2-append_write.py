#!/usr/bin/python3
""" creating a function to append a file """


def append_write(filename="", text=""):
    """
    append a strinfg to a text file (UFT-8) and return the number of characters

    Args:
        filename (str): The name of the file to write
        text (str): The string to append to a file

    Returns:
        int: The number of characters appended to the file
    """

    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
