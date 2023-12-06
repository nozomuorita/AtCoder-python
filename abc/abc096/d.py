from collections import defaultdict
def eratosthenes_sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for p in range(2, n+1):
        if is_prime[p]:
            for q in range(2*p, n+1, p):
                is_prime[q] = False
    return is_prime

n = int(input())
e = eratosthenes_sieve(55556)
prime = []
for i in range(len(e)):
    if e[i]: prime.append(i)

d = defaultdict(list) # key: 余り, value: 素数
for p in prime:
    d[p%5].append(p)
    if len(d[p%5])==n: exit(print(*d[p%5]))