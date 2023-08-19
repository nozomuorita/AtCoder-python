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
# round関数を使ってしまうと5付近の丸め込みに失敗する
# 文字列で管理
X = input()

for i in range(len(X)):
    if X[i]=='.':
        n = i
        break

if int(X[n+1])<=4:
    print(X[:n])
else:
    ans = int(X[:n])
    print(ans + 1)