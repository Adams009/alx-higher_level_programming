#!/usr/bin/python3
""" script that adds all arguments to a Python list """
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_items_to_list_and_save():
    """
    Add all command-line arguments to a Python list and save it to a file
    The file is named add_item.json.
    If the file doesn't exist, it will be created.
    """
    try:
        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []
    existing_list.extend(sys.argv[1:])
    save_to_json_file(existing_list, "add_item.json")
