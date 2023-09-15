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
s1 = input()
s2 = input()
s3 = input()
t = list(input())

ans = []
for i in t:
    if i=='1':
        ans.append(s1)
    elif i=='2':
        ans.append(s2)
    else:
        ans.append(s3)

print(''.join(ans))