#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    for key, myvalue in a_dictionary.items():
        if (myvalue == value):
            a_dictionary.pop(key)
            break
