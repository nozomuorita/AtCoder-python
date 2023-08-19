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
b = list(map(int, input().split()))

d = [] # 差分

for i in range(n):
    d.append(abs(a[i]-b[i]))

d_sum = sum(d)
# 差分の和がkより大きいなら、そもそも不可
if d_sum>k:
    print('No')
    exit()

d_sum -= k
# k以上の分が偶数回残っているなら可(同じところを足して引いてをすれば変わらない)
if d_sum%2==0:
    print('Yes')
else:
    print('No')