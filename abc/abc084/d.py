"""
・10**5までの素数で条件を満たすものをリストに入れる
・そのリストからlとrを二分探索する
・そのときのインデックスの差が答え
"""
from bisect import bisect_left, bisect_right, insort_left, insort_right
def eratosthenes_sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for p in range(2, n+1):
        if is_prime[p]:
            for q in range(2*p, n+1, p):
                is_prime[q] = False
    return is_prime

primes = eratosthenes_sieve(10**5+1)
lst = []
for i in range(2, 10**5+1):
    if i%2==1 and primes[i] and primes[(i+1)//2]:
        lst.append(i)

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    left = bisect_left(lst, l)
    right = bisect_right(lst, r)
    
    print(right-left)