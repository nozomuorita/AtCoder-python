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
n, X = map(int, input().split())
x = list(map(int, input().split()))

# 都市が一つだけなら、その都市との差を出力して終了
if n == 1:
    print(abs(X-x[0]))
    exit()

dx = []
for i in range(n):
    dx.append(abs(X-x[i]))

g = math.gcd(dx[0], dx[1])
for i in range(2, n):
    g = math.gcd(g, dx[i])

print(g)