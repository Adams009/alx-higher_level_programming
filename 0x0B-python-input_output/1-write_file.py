#!/usr/bin/python3
""" creating a function to write a  test to afile """


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and return the number of characters

     Args:
    filename (str): The name of the file to write
    text (str): The string to write to the file.

     Returns:
        int: The number of characters written to the file.
     """

    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
