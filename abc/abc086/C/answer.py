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
t = []
xy = []

for i in range(n):
    _ = list(map(int, input().split()))
    t_ = _[0]
    xy_ = [_[1], _[2]]
    t.append(t_)
    xy.append(xy_)

s = [0, 0]
d = []
for i in range(n):
    tmp = xy[i]
    dist = abs(s[0]-tmp[0]) + abs(s[1]-tmp[1])
    d.append(dist)
    s = tmp

s_t = 0
t_d = []
for i in range(n):
    t_d.append(t[i]-s_t)
    s_t = t[i]

# print(d)
# print(t_d)
f = True
for i in range(n):
    if d[i]>t_d[i]:
        f = False
        break
    if (d[i]%2) != (t_d[i]%2):
        f = False
        break

if f:
    print('Yes')
else:
    print('No')