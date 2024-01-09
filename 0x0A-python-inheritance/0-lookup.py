#!/usr/bin/python
""" This module retrives all attributes """


def lookup(obj):
    """
    Returns a list containing the names of attributes and methods

    Args:
        obj: The object to inspect.

    Returns:
        list: A list containing the names of attributes and methods.
    """

    return dir(obj)
