#!/usr/bin/python3

""" Using the requests module to tests get """

import requests


if __name__ == "__main__":

    r = requests.get("https://alx-intranet.hbtn.io/status")
    text = r.content.decode("utf-8")

    print("Body response:")
    print("\t- type:", type(text))
    print("\t- content:", text)
