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
s, t = [], []
for i in range(n):
    s_, t_ = map(str, input().split())
    s.append(s_)
    t.append(t_)

flag = True

for i in range(n):
    name1 = s[i]
    name2 = t[i]
    other = s[:i] + s[i+1:] + t[:i] + t[i+1:]
    if (name1 in other) and (name2 in other):
        flag = False
        break
        
if flag:
    print('Yes')
else:
    print('No')