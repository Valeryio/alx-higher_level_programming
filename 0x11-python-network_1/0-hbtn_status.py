#!/usr/bin/python3

""" This file make a request with urllib """

import urllib.request


url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    result = response.read()
    print("Body response:"
            "\n\t- type:", type(result),
            "\n\t- content:", result,
            "\n\t- utf8 content:", response.msg)
