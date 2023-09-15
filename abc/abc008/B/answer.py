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
d = defaultdict(int)

for i in range(n):
    s = input()
    d[s] += 1
    
mx = -1
for i in list(d.keys()):
    if d[i] > mx:
        ans = i
        mx = d[i]
        
print(ans)