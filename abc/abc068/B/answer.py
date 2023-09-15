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

ans = 1
mx = 0
n = int(input())
for i in range(1, n+1):
    c = collections.Counter(prime_factorize(i))
    if mx < c[2]:
        mx = c[2]
        ans = i
print(ans)