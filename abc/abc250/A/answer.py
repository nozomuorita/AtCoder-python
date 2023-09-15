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
H, W = map(int, input().split())
R, C = map(int, input().split())

ans = 0
for i, j in [[R+1, C], [R-1, C], [R, C+1], [R, C-1]]:
    if (1<=i<=H) and (1<=j<=W):
        ans += 1

print(ans)