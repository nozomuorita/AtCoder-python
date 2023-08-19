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
s1 = [1]

if N == 1:
    print(1)
    exit()

for i in range(2, N+1):
    s2 = i
    s = s1.copy()
    s.append(s2)
    s.extend(s1)
    
    s1 = s

print(*s)