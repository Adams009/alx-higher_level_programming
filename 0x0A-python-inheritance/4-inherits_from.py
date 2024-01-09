#!/usr/bin/python3
""" check if an object is an instance of a class diectly or indirectlu"""


def inherits_from(obj, a_class):
    """
     Returns True if the object is an instance of a class that inherited

     Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class

