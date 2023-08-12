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
a, b, w = map(int, input().split())
w *= 1000

# n個買うことができるかを調べる。
# 最大で1 * 1000 * 1000

mn = 10**9
mx = 0
for i in range(1, 1000*1000+1):
    if a*i <= w <= b*i:
        mn = min(mn, i)
        mx = max(mx, i)

if mx == 0:
    print('UNSATISFIABLE')
else:
    print(mn, mx)