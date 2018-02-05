#!/bin/python3

import sys
import math

a = []
a.append(2)

for i in range(3, 110000, 2):
    cont = 0
    for j in range(1, int(math.sqrt(i)+1), 2):
        if i % j == 0:
            cont += 1
    if cont == 1:
        a.append(i)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(a[n-1])