#!/usr/bin/python3
"""
    This module adds new arguments, to a json file
"""
import json
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if not os.path.exists('add_item.json'):
    # Write directly for the first time
    save_to_json_file(sys.argv[1:], "add_item.json")

else:
    # Upload the data as python object from the file
    data = load_from_json_file("add_item.json")

    # Appending new object to the object
    for i in sys.argv[1:]:
        data.append(i)

    # Write the object as json in the json's file
    save_to_json_file(data, "add_item.json")
