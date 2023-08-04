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
import functools
inf = float('inf')
mod1 = 10**9+7
mod2 = 998244353
def ceil_div(x, y): return -(-x//y) # 切り上げ
def my_gcd(*integers): return functools.reduce(math.gcd, integers)

# main code ------------------------------------------------------------------------------------
k = int(input())
ans = 0

for a in range(1, k+1):
    for b in range(1, k+1):
        for c in range(1, k+1):
            ans += my_gcd(a, b, c)
            
print(ans)