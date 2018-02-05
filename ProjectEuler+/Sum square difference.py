#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    sum_to_n = (n*(n+1))/2
    sum_to_n_square = int(sum_to_n ** 2)

    sum_square_to_n = int((n*(n+1)*(2*n+1))/6)

    print(sum_to_n_square-sum_square_to_n)

