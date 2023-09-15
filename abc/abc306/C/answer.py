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
N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
ans = []

for i in range(len(A)):
    tmp = A[i]
    d[tmp] += 1
    if d[tmp] == 2:
        ans.append(tmp)
    
print(*ans)