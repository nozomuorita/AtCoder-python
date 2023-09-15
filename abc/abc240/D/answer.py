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

d = []
boll = 0

for i in a:
    boll += 1
    print(d)
    if len(d)==0:
        d.append([i, 1])
    else:
        if d[-1][0] == i:
            d[-1][1] += 1
        else:
            d.append([i, 1])

        while d:
            if d[-1][0]==d[-1][1]:
                num1, num2 = d.pop()
                boll -= num2
            else:
                break

    print(boll)