#!/usr/bin/python3
""" creating a function to represent JSON of an object """
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized to JSON.

    Returns:
        str: The JSON representation of the input object.
    """
    return json.dumps(my_obj)
