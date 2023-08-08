# @nzm_ort
# https://github.com/nozomuorita/atcoder-workspace-python

# import module ------------------------------------------------------------------------------
from collections import defaultdict, deque, Counter
import math
from itertools import combinations, permutations, product, accumulate, groupby, chain
from heapq import heapify, heappop, heappush
import bisect
import sys
#sys.setrecursionlimit(100000000)
inf = float('inf')
mod1 = 10**9+7
mod2 = 998244353
def ceil_div(x, y): return -(-x//y)

# main code ------------------------------------------------------------------------------------
k = int(input())

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

def f(n, p):
    if n==0:
        return 0
    n //= p
    return n + f(n, p)

p = prime_factorize(k)
c = Counter(p)

ac, wa = k, 0
while (ac-wa > 1):
    wj = (ac+wa) // 2
    ok = True
    for p in list(c.keys()):
        cnt = c[p]
        if f(wj, p) < cnt:
            ok = False

    if ok:
        ac = wj
    else:
        wa = wj

print(ac)