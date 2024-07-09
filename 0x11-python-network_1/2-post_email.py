#!/usr/bin/python3

""" This module makes a post request """

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    mail = sys.argv[2]

    value = {"email": mail}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode("utf-8")
    print(the_page)
