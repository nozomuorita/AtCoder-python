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
def ceil_div(x, y): return -(-x//y) # 切り上げ

# main code ------------------------------------------------------------------------------------
n, k = map(int, input().split())
c = list(map(int, input().split()))

d = {}
for i in range(k):
    if c[i] in d:
        d[c[i]] += 1
    else:
        d[c[i]] = 1

ans = len(d)

for i in range(n-k):
    d[c[i]] -= 1
    if d[c[i]] == 0:
        del d[c[i]]
    if c[i+k] in d:
        d[c[i+k]] += 1
    else:
        d[c[i+k]] = 1
    
    if len(d) > ans:
        ans = len(d)

print(ans)