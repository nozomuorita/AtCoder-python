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
# Pythonで提出(PypyはMLE)
p = list(map(int, input().split()))
p1 = [p[0], p[1]]
p2 = [p[2], p[3]]
p3 = [p[4], p[5]]

if p1==[0, 0]:
    ans = abs((p2[0]*p3[1]) - (p2[1]*p3[0])) / 2
elif p2==[0, 0]:
    ans = abs((p1[0]*p3[1]) - (p1[1]*p3[0])) / 2
elif p3==[0, 0]:
    ans = abs((p1[0]*p2[1]) - (p1[1]*p2[0])) / 2
else:
    ans = abs((p1[0]-p3[0])*(p2[1]-p3[1]) - (p2[0]-p3[0])*(p1[1]-p3[1])) / 2

print(ans)