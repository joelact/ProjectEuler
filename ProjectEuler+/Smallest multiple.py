#!/bin/python3

import sys
import fractions

def result(n):
    lcm = 1
    for i in range(1, n + 1):
        lcm = (lcm * i)/fractions.gcd(lcm, i)
    
    return int(lcm)
    


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(result(n))