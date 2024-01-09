#!/usr/bin/python3
""" This module to check if an object is an instance of or inherited"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of or inherited

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance of or inherited from a_class
    """

    return isinstance(obj, a_class)
