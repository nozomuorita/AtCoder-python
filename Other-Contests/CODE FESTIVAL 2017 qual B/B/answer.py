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
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

prob = defaultdict(int)
for i in range(n):
    prob[d[i]] += 1

for i in range(m):
    if prob[t[i]] == 0:
        print('NO')
        exit()
    else:
        prob[t[i]] -= 1

print('YES')