#!/usr/bin/python3
"""  function that creates an Object from a “JSON file”  """
import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python data structure represented by the JSON file.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
