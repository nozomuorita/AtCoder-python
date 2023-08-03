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
s, t = map(int, input().split())
ans = 0

for i in range(101):
    for j in range(101):
        for k in range(101):
            if (i+j+k<=s) and (i*j*k<=t):
                ans += 1

print(ans)