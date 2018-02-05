t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    soma = 0
    i = 1
    j = 0
    f = 0
    while i < n:
        if f % 2 == 0:
            soma += f
        f = i + j
        j = i
        i = f
        
    print(soma)