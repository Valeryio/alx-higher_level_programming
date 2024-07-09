#!/usr/bin/python3

""" This module gets the X-Request-Id of a header """

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        new_dict = {}
        for key, value in response.getheaders():
            new_dict.setdefault(key, value)

        print(new_dict["X-Request-Id"])
