#!/usr/bin/python3

# This module gets the header of a requests

import sys
import urllib.request


url = sys.argv[1]
mail = sys.argv[2]

value = {"email": mail}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data)

with urllib.request.urlopen(req) as response:
    the_page = response.read()
    print(the_page)
