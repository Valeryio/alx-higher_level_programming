#!/usr/bin/python3

for i in range(65, 91):
    if (i != 69 and i != 81):
        print('{n}'.format(n=chr(i).lower()), end='')
