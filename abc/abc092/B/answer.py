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
n = int(input())
d, x = map(int, input().split())
a = [int(input()) for i in range(n)]

ans = 0
for i in range(n):
    k = 0
    while (k*a[i]+1 <= d):
        ans += 1
        k += 1

print(ans+x)