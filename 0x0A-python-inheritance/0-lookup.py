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

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods = [attr for attr in dir(obj) if callable(getattr(obj, attr)) and not attr.startswith("__")]

    return attributes + methods
