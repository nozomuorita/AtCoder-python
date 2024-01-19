"""エラトステネスの篩"""
def eratosthenes_sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for p in range(2, n+1):
        if is_prime[p]:
            for q in range(2*p, n+1, p):
                is_prime[q] = False
    return is_prime

q = int(input())
prime = eratosthenes_sieve(300000)
for _ in range(q):
    x = int(input())
    print('Yes') if prime[x] else print('No')