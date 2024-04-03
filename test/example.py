#!/usr/bin/python3

def add(x, y):
    return x + y

x = 1
y = 2
# lamba <variables in input> : <single operation on variable that will be returned>

print("We have x + y = ",int({lambda x, y: x + y}))
