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
n=int(input())
s=list(map(int, input().split()))
ans=0

for i in range(n):
    si=s[i]
    f = False

    for a in range(1, si+1):
        for b in range(1, si+1):
            if (4*a*b+3*a+3*b)==si:
                f = True
    
    if f:
        continue
    else:
        ans+=1

print(ans)