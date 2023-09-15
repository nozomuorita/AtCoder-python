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
n = int(input())
a = list(map(int, input().split()))

dig = [0]
for i in a:
    dig.append((dig[-1]+i)%360)
dig.sort()
dig.append(360)
dist = []

for i in range(1, len(dig)):
    dist.append(dig[i]-dig[i-1])

print(max(dist))