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
X, Y, Z = map(int, input().split())

if (Y < 0):
  X *= -1
  Y *= -1
  Z *= -1
  
if X < Y:
  # 直接行ける
  print(abs(X))
  
else:
  if (Z < Y) and (Z > 0):
    print(abs(X))
  elif (Z < Y) and (Z < 0):
    ans = 2 * abs(Z) + abs(X)
    print(ans)
  else:
    print(-1)