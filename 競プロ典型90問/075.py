"""
・素因数分解して考える
・素因数分解したときの素因数の個数をカウントし、numとしておく
・今回の操作は1回の魔法で2つに、2回の魔法で4つまで分解されるといった流れになる
・ゆえに1回魔法を使うごとに1, 2, 4, 8, 16と個数を増やせるということになる
・なので素因数の個数をnum個としたとき、このnumを超える最小の魔法回数を求めることで答えとなる
・ex) n=42のとき
・42=2*3*7であるため、素因数の個数は3個である。
・1回魔法を使うことで42を二つに、2回魔法を使うことで42を4つに分解できるため、すべて素数にするためには最低2回魔法を使う必要がある。
"""
import collections
n = int(input())

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

c = collections.Counter(prime_factorize(n))
num = 0
for i in c.keys():
    num += c[i]
    
if num==1:
    print(0)
else:
    ans = 0
    m = 1
    while m<num:
        ans += 1
        m *= 2
    print(ans)