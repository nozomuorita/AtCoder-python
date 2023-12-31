"""
・pを素因数分解して数える
・pにある素因数aがn個あるならaを1個ずつ割り振ることで最大公約数に含めることができる
・2*n個あるならそれぞれにa*aを割り振ることができる
・ゆえに、ans=1で初期化し、ある素因数aをb個割り振ることができるならans*=(a**b)とする。
"""
from collections import Counter
n, p = map(int, input().split())

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
    return a

c = Counter(prime_factorize(p))
ans = 1
for key in list(c.keys()):
    if c[key]//n>0: ans *= (key ** (c[key]//n))

print(ans)