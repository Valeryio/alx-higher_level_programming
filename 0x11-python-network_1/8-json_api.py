#!/usr/bin/python3

""" THis is a program to test json api of the requests module """

import requests
import sys

if __name__ == "__main__":

    try:
        param = sys.argv[1]
    except IndexError:
        param = ""

    value = {"q": param}

    r = requests.post("http://0.0.0.0:5000/search_user", data=value)
    result = r.text
    result = dict(result)

    if type(r.json()) is not dict:
        print("Not a valid JSON")
    elif r.json() == {}:
        print("No result")
    else:
        print("[{}] {}".format(r.json()['id'], r.json()['name']))
