# @nzm_ort
# https://github.com/nozomuorita/atcoder-workspace-python

# import module ------------------------------------------------------------------------------
from collections import defaultdict, deque, Counter
import math
from itertools import combinations, permutations, product, accumulate, groupby, chain
from heapq import heapify, heappop, heappush
import bisect
import sys
# sys.setrecursionlimit(100000000)
inf = float('inf')
mod1 = 10**9+7
mod2 = 998244353
def ceil_div(x, y): return -(-x//y) 

# main code ------------------------------------------------------------------------------------
n, m = map(int, input().split())
s = input()
c = list(map(int, input().split()))

m_appear = [False] * m
d = defaultdict(int)
d_str = defaultdict(list)

ans = ''

for i in range(n):
    #d[c[i]] += 1
    d_str[c[i]] += s[i]

for i in range(n):
    tmp = c[i]
    if not(m_appear[tmp-1]):
        ans += d_str[tmp][-1]
        m_appear[tmp-1] = True
        d[c[i]] += 1
    else:
        ans += d_str[tmp][d[c[i]]-1]
        d[c[i]] += 1

print(ans)