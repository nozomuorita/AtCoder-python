from collections import Counter
n = int(input())

prime = [0]*n    # prime[i]: 数字iとなるA, Bの組の個数
prime[1] = 1

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

for i in range(2, n):
    c = Counter(prime_factorize(i))
    num = 1
    for key in list(c.keys()):
        num *= c[key]+1
    prime[i] = num
    
ans = 0
for i in range(1, n):
    ans += prime[i] * prime[n-i]
print(ans)