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
S = list(input())

up = False
low = False

for i in S:
    if ord('A') <= ord(i) <= ord('Z'):
        up = True
    if ord('a') <= ord(i) <= ord('z'):
        low = True
        
if up and low:
    l_origin = len(S)
    S_set = set(S)
    if len(S_set) == l_origin:
        print('Yes')
    else:
        print('No')
    
else:
    print('No')