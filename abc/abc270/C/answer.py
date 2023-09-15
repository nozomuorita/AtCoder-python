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
n, x, y = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(n-1):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

x -= 1
y -= 1
visited = [False] * n

q = deque()
q.append(x)
# 探索時に親の情報も求める
# -2はスタート地点であることを示す
parent = [-1] * n
parent[x] = -2

while q:
    p = q.popleft()
    visited[p] = True

    if p==y:
        break

    for i in g[p]:
        if visited[i]:
            continue
        parent[i] = p
        q.append(i)

# ゴールから親情報をたどる
ans = [y]
s = y
while s != -2:
    ans.append(parent[s])
    s = parent[s]

ans = [i+1 for i in ans]
print(*reversed(ans[:-1]))