#!/usr/bin/python3

# This module gets the header of a requests

import sys
import urllib.request


url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    new_dict = {}
    for key, value in response.getheaders():
        new_dict.setdefault(key, value)

    print(new_dict["X-Request-Id"])
