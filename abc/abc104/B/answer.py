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
s = input()

if s[0] != 'A':
    print('WA')
    exit()

idx = []
for i in range(len(s)):
    if s[i] == 'C':
        idx.append(i)

if (len(idx)!=1) or not(2<=idx[0]<=len(s)-2):
    print('WA')
    exit()

idx = idx[0]
for i in range(1, len(s)):
    if i == idx:
        continue
    else:
        if s[i].islower():
            continue
        else:
            print('WA')
            exit()

print('AC')