#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = str(input().strip())

    total_elem = n - k
    p_max = 0

    for i in range(total_elem + 1):
        temp = i + k
        string = num[i:temp]
        product = 1
        for j in string:
            product *= int(j)

        if product > p_max:
            p_max = product
    
    print(p_max)



