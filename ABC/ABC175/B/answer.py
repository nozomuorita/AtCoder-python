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
l = list(map(int, input().split()))
ans = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if (i==j) or (j==k) or (k==i):
                continue
            if (l[i] != l[j]) and (l[j] != l[k]) and (l[k] != l[i]):
                # ある辺の長さは、他の二辺の和よりも小さい
                if(l[i]<l[j]+l[k]) and (l[j]<l[i]+l[k]) and (l[k]<l[i]+l[j]):
                    ans += 1

print(ans)