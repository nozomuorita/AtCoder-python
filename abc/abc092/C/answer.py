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
a = list(map(int, input().split()))

# すべて訪れる場合の料金を計算しておく
fee = abs(a[0])
for i in range(n-1):
    fee += abs(a[i] - a[i+1])
fee += abs(a[-1])

ans = []
for i in range(n):
    if i==0:
        tmp1 = 0
    else:
        tmp1 = a[i-1]
    
    tmp2 = a[i]

    if i==(n-1):
        tmp3 = 0
    else:
        tmp3 = a[i+1]

    abs1 = abs(tmp1-tmp2)
    abs2 = abs(tmp2-tmp3)
    abs3 = abs(tmp1-tmp3)

    ans.append(fee-abs1-abs2+abs3)

for i in range(n): print(ans[i])