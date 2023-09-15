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
h, w, C, q = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(q)]

row = set()
col = set()
color = [0] * C
for i in reversed(range(q)):
    t, n, c = query[i][0], query[i][1], query[i][2]
    if t == 1:
        if n in row:
            continue
        row.add(n)
        color[c-1] += w - len(col)
    else:
        if n in col:
            continue
        col.add(n)
        color[c-1] += h - len(row)

print(*color)