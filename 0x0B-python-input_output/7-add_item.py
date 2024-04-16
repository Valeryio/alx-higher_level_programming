#!/usr/bin/python3
"""
    This module adds new arguments, to a json file
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file



# Open the file with the appending
with open("add_item.json", 'a', encoding="UTF-8") as json_file:
    data = load_from_json_file(add)

    for i in sys.argv[1:]:
        data.append(i)



#    save_to_json_file(sys.argv[1:], "myfile.txt")
# Deserialize from this tmp file

#   json.dump(data, json_file)
