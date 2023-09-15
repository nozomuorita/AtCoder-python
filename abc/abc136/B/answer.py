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
n_str = str(n)

k = 1
ans = 0
while k<10**(len(n_str)-1):
    if len(str(k))%2==1:
        ans += 9*k
    k *= 10

if len(n_str)%2==1:
    ans += n - (10**(len(n_str)-1)) + 1

print(ans)