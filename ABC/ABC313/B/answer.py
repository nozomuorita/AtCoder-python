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
n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

st = [[] for _ in range(n)]

for i in range(m):
    a = ab[i][0] - 1
    b = ab[i][1] - 1

    st[a].append(b)
#print(st)
ans = []
for i in range(n):
    win = set()
    q = deque()
    for j in st[i]:
        q.append(j)
    while q:
        num = q.popleft()
        if num in win:
            continue
        win.add(num)
        for k in st[num]:
            if k not in win:
                q.append(k)
       # print(num, win, q)

    if len(win)==(n-1):
        ans.append(i+1)

if len(ans)==1:
    print(ans[0])
else:
    print(-1)
