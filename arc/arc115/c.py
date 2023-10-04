"""
・各数について、素因数の数+1が答えとなる
"""

n = int(input())
ans = []

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return len(a)

for i in range(1, n+1):
    ans.append(prime_factorize(i)+1)
    
print(*ans)