from collections import defaultdict, Counter
n = int(input())
mod = 10**9+7

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

d = defaultdict(int)
for i in range(2, n+1):
    c = Counter(prime_factorize(i))
    for key in c.keys():
        d[key] += c[key]

ans = 1
for key in list(d.keys()):
    ans *= d[key]+1
    ans %= mod

print(ans)