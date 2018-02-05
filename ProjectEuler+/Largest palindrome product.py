#!/bin/python3

import sys

a = []

for i in range(100, 1000):
    for j in range(100, 1000):
        number = i * j
        if number > 101100 and number < 1000000:
            s_number = str(number)
            r_number = s_number[::-1]
            if s_number == r_number:
                a.append(number)


a.sort()
a.reverse()

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for i in a:
        if i < n:
            print(i)
            break
