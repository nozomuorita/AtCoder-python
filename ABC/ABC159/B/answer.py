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
s_r = s[::-1]

if s != s_r:
    print('No')
    exit()

s2 = s[:(len(s)-1)//2]
s2_r = s2[::-1]
if s2 != s2_r:
    print('No')
    exit()
    
s3 = s[(len(s)+3)//2-1:]
s3_r = s3[::-1]
if s3 != s3_r:
    print('No')
    exit()
    
print('Yes')