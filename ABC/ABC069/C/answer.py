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
a = list(map(int, input().split()))

sum_ = 0
for i in a:
    if i%4 == 0:
        sum_ += 2
    elif i%2 == 0:
        sum_ += 1
    else:
        continue

if n%2==0:
    if sum_ >= n:
        print('Yes')
    else:
        print('No')
else:
    if sum_ >= n-1:
        print('Yes')
    else:
        print('No')