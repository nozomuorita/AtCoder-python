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
n, k  = map(int, input().split())
s = [input() for i in range(n)]

ans = 0

# bit全探索
for i in range(2**n):
    d = defaultdict(int)
    num = 0 # k個登場する文字の種類
    for j in range(n):
        if ((i >> j) & 1):
            #num += 1
            for m in s[j]:
                d[m] += 1
    
    for i in list(d.keys()):
        if d[i] == k:
            num += 1
            
    if ans < num:
        ans = num

print(ans)