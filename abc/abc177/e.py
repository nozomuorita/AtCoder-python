"""公式解説"""
from math import gcd

n = int(input())
a = list(map(int, input().split()))
f1, f2 = True, True

def prime_factorize(n):
    a = set()
    while n % 2 == 0:
        a.add(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.add(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.add(n)
    return a

s = set()
for i in range(n):
    prime = prime_factorize(a[i])
    if len(s&prime)>=1: f1=False; break
    s |= prime
    
g = a[0]
for i in range(1, n):
    g = gcd(g, a[i])
if g!=1: f2=False

if f1: print("pairwise coprime")
elif f2: print("setwise coprime")
else: print("not coprime")