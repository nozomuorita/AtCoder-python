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
s = int(input())

a = [s]

while True:
    if a[-1]%2 == 0:
        if a[-1]//2 in a:
            a.append(a[-1]//2)
            break
        else:
            a.append(a[-1]//2)
    else:
        if 3*a[-1]+1 in a:
            a.append(3*a[-1]+1)
            break
        else:
            a.append(3*a[-1]+1)

print(len(a))