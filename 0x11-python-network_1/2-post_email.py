#!/usr/bin/python3

"""This module makes a post request"""

import sys
import urllib.request


url = sys.argv[1]
mail = sys.argv[2]

value = {"email": mail}
data = urllib.parse.urlencode(value)
data = data.encode('ascii')
req = urllib.request.Request(url, data)

with urllib.request.urlopen(req) as response:
    the_page = response.read()
    print(the_page)
