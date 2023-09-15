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
a = list(map(int, input().split()))

# parent: 世代を管理
parent = [0] * (2*(n)+1)

for i in range(1, n+1):
    # 新たに生成されるアメーバの世代は、生成元の世代数＋１となるため更新
    parent[2*i-1], parent[2*i] = parent[a[i-1]-1]+1, parent[a[i-1]-1]+1

for i in range(2*n+1):
    print(parent[i])