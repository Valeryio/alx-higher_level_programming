#!/usr/bin/python3

""" This file make a request with urllib """

import urllib.request


if __name__ == "__main__":

    url = "https://alx-intranet.hbtn.io/status"
#    url = "http://0.0.0.0:5000"

    with urllib.request.urlopen(url) as response:
        result = response.read()
        print("Body response:")
        print("\t- type:", type(result))
        print("\t- content:", result)
        print("\t- utf8 content:", response.msg)
