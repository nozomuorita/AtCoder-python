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
a = []
c = []

for i in range(n):
    c_ = int(input())
    a_ = list(map(int, input().split()))

    c.append(c_)
    a.append(a_)

x = int(input())

d = defaultdict(int)
for i in range(n):
    if x in a[i]:
        tmp = len(a[i])
        d[i] = tmp

if len(list(d.keys()))==0:
    print(0)
    exit()

mn = min(list(d.values()))
#print(d)

ans = []
for i in list(d.keys()):
    if d[i] == mn:
        ans.append(i+1)
print(len(ans))
print(*ans)