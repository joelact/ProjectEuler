#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    soma = 0
    p = (n-1)//3
    soma = ((3*p*(p+1))//2)

    p = (n-1)//5
    soma += ((5*p*(p+1))//2)

    p = (n-1)//15
    soma -= ((15*p*(p+1))//2)
    print(soma)