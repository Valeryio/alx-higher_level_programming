#!/usr/bin/python3

import calculator_1 as calc

a = 10
b = 5

print("{i} + {j} = {k}".format(i=a, j=b, k=calc.add(a, b)))
print("{i} - {j} = {k}".format(i=a, j=b, k=calc.sub(a, b)))
print("{i} * {j} = {k}".format(i=a, j=b, k=calc.mul(a, b)))
print("{i} / {j} = {k}".format(i=a, j=b, k=calc.div(a, b)))
