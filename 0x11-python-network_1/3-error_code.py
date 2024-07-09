#!/usr/bin/python3

""" This code send a request to an url and manage the exceptions
    with HTTPError from the urllib library """

import sys
import urllib.request
import urllib.error


url = sys.argv[1]
try:
    with urllib.request.urlopen(url) as response:
        result = response.read().decode("utf-8")
        print(result)
except urllib.error.HTTPError as Error:
    print("Error code:", Error.status)
