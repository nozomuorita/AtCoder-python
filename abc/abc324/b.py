"""
・素因数分解
・素因数が2、3のみならYes(片方でもok)
"""
import collections
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


n = int(input())
# n=1ならYes
if n==1:
    print('Yes')
    exit()

c = collections.Counter(prime_factorize(n))
keys = list(c.keys())

if len(keys)==2:
    if (2 in keys) and (3 in keys):
        print('Yes')
    else:
        print('No')
elif len(keys)==1:
    if keys[0]==2 or keys[0]==3:
        print('Yes')
    else:
        print('No')
else:
    print('No')
    