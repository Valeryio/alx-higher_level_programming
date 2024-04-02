#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{}".format(int(value)))
        return True
    except ValueError:
        return False
