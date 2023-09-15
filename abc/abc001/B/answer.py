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
m = int(input())
m /= 1000

if m < 0.1:
    ans = '00'
elif m <= 5:
    ans = str(int(m * 10))
    if len(ans)==1:
        ans = '0' + ans
elif m <= 30:
    ans = str(int(m + 50))
elif m <= 70:
    ans = str(int((m - 30) / 5 + 80))
else:
    ans = '89'

print(ans)