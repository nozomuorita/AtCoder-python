"""
・素数判定・列挙(is_prime, eratosthenes_sieve)
・素因数分解(prime_factorize)
・約数列挙(make_divisors)
"""

#  素数判定(試し割り法O(√n))
#  2から√Nまで順に割っていき，割り切れたら素数ではない

# ↓は間違っているっぽい
def is_prime(n):
    if n == 1:
        return True
    if n%2 ==0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#  ↓が正しい
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# print(is_prime(5))
# >> True


#  素数列挙(エラトステネスの篩O(nlog(logn)))
#  n以下の素数を全列挙する
#  判定を複数行う場合，前処理後はO(1)で判定可能
#  デメリット：大きさNの配列を使うため，メモリ大
#  方法：小さいほうから素数判定し，その数が素数ならば，その倍数をすべて削除(素数ではないため)
def eratosthenes_sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for p in range(2, n+1):
        if is_prime[p]:
            for q in range(2*p, n+1, p):
                is_prime[q] = False
    return is_prime

# print(eratosthenes_sieve(10))
# >> [False, False, True, True, False, True, False, True, False, False, False]


#  素因数列挙
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

# prime_factorize(1)
# >> []

# prime_factorize(280)
# >> [2, 2, 2, 5, 7]


#  素数とその個数を取得
#  key: 素因数, value: 素べき
from collections import Counter

#  c = Counter(prime_factorize(840))
#  print(c)
#  >> Counter({2: 3, 3: 1, 5: 1, 7: 1})

# 約数列挙
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

#  make_divisors(10)
#  >> [1, 2, 5, 10]

#  n!をpで何回割れるか
def f(n, p):
    if n==0:
        return 0
    n //= p
    return n + f(n, p)

#  5!を2で何回割れるか(3回)
#  f(5, 2)
#  >> 3