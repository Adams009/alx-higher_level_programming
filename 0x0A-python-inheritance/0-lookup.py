#!/usr/bin/python3
"""
This module provides a function to retrieve the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list containing the names of attributes and methods of the given object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list containing the names of attributes and methods.
    """

    return [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
