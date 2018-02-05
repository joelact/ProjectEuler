from math import *

def primo(n):
    soma = 0
    for i in range(1, floor(sqrt(n)) + 1):
        if n % i == 0:
            soma += 1
    return soma        


t = int(input().strip())
for a0 in range(t):
    k = 0
    tra = 0
    n = int(input().strip())
    a = []
    
    if primo(n) == 1:
        print(n)
    else:
        for i in range(1, floor(sqrt(n)) + 1):
            if n % i == 0:
                a.append(i)
                l = n / i
                a.append(l)
        for j in a:
            if primo(j) == 1:
                k = floor(j)
                if k > tra:
                    tra = k
        print(tra)        
                