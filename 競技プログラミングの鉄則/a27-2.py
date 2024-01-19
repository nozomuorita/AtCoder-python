"""素因数使用"""
from collections import Counter
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
        else: f += 2
    if n != 1: a.append(n)
    return a

a, b = map(int, input().split())
c1 = Counter(prime_factorize(a))
c2 = Counter(prime_factorize(b))

ans = 1
for key in list(c1.keys()):
    if c2[key]>0: ans*=(key ** min(c1[key], c2[key]))

print(ans)