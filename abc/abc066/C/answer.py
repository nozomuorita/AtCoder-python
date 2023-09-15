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

l1 = [] # odd
l2 = [] # even

for i in range(len(a)):
    if (i+1)%2==0:
        l2.append(a[i])
    else:
        l1.append(a[i])

if n%2==0:
    l2 = list(reversed(l2))
    print(*l2, *l1)
else:
    l1 = list(reversed(l1))
    print(*l1, *l2)