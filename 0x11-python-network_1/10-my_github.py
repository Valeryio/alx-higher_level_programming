#!/usr/bin/python3

""" This program use some of my credentials to get my github ID """

import sys
import requests


if __name__ == "__main__":

    username = sys.argv[1]
    token = sys.argv[2]
#    values = {"username": sys.argv[1], "password": sys.argv[2]}
    r = requests.get(f"https://api.github.com/users/{username}")

    if r.status_code == 200:
        print(r.json()['id'])
