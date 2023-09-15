# @nzm_ort
# https://github.com/nozomuorita/atcoder-workspace-python

# import module ------------------------------------------------------------------------------
from collections import defaultdict, deque, Counter
import math
from itertools import combinations, permutations, product, accumulate, groupby, chain
from heapq import heapify, heappop, heappush
from bisect import bisect_left, bisect_right
import sys
# sys.setrecursionlimit(100000000)
inf = float('inf')
mod1 = 10**9+7
mod2 = 998244353
def ceil_div(x, y): return -(-x//y) # 切り上げ

# main code ------------------------------------------------------------------------------------
n, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort()
a, b = [], []
for i in range(n):
    a.append(ab[i][0])
    b.append(ab[i][1])

# 累積和
b_sum = [0]
for i in range(n):
    b_sum.append(b_sum[i]+b[i])

ans = 0
pre = 0

while k != 0:
    ans += k
    k -= k
    
    # 二分探索
    idx = bisect_right(a, ans)
    money = b_sum[idx] - b_sum[pre]
    k += money
    pre = idx

print(ans)