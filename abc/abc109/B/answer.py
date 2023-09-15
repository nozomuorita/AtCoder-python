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
w = [input() for _ in range(n)]

said = set()
for i in range(n):
    if i==0:
        said.add(w[i])
    else:
        if w[i] in said:
            print('No')
            exit()
        if w[i-1][-1] != w[i][0]:
            print('No')
            exit()
        said.add(w[i])

print('Yes')