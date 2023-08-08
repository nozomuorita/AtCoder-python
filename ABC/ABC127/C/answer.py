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
n, m = map(int, input().split())
lr = [list(map(int, input().split())) for i in range(m)]

mn = lr[0][0]
mx = lr[0][1]

for i in range(1, m):
    l = lr[i][0]
    r = lr[i][1]

    if l > mn:
        mn = l
    if r < mx:
        mx = r

if mn <= mx:
    print(mx-mn+1)
else:
    print(0)