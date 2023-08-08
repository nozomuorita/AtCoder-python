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
n, k = map(int, input().split())
a = list(map(int, input().split()))

idx = a.index(1)
left = idx
right = n - idx - 1

num = left + right
ans = ceil_div(num, (k-1))

print(ans)