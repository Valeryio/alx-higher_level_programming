#!/usr/bin/python3

""" This is a new test on get requests """

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    r = requests.get(url)

    try:
        attended_header = r.headers["X-Request-Id"]
        print(attended_header)
    except KeyError:
        pass
