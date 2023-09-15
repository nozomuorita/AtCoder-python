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
# A+K-1番目の人が最後になる
# ただし、循環する場合はNで割ったあまりが答え
# 余りが0の場合は、一番最後にいる人なので、Nとなる
N, K, A = map(int, input().split())

ans = (A+K-1) % N
print(ans if ans!=0 else N)