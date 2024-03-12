#!/usr/bin/python3

for i in range(100):
    print(f"{i:0>2d}", end='')
    if (i + 1 != 100):
        print(f", ", end="")
