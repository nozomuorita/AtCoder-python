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
xy = []
for i in range(n):
    xy_ = list(map(int, input().split()))
    xy.append(xy_)

# dp[i][j]: i番目まで食べて、おなかの状態がjのときのおいしさの最大値
# j: (0: おなかを壊していない), (1: おなかを壊している)
dp = [[0, 0] for _ in range(n+1)]

# おいしさにマイナスもある点に注意
for i in range(n):
    if xy[i][0]==0:
        # (おなかを壊していない状態で食べる, おなかを壊している状態で食べる, おなかを壊していない状態で食べない)
        dp[i+1][0] = max(dp[i][0]+xy[i][1], dp[i][1]+xy[i][1], dp[i][0])
        # 選択肢は、おなかを壊している状態でたべないのみ
        dp[i+1][1] = dp[i][1]
    else:
        # おなかを壊していない状態で食べないのみ
        dp[i+1][0] = dp[i][0]
        # (おなかを壊していない状態で食べる, おなかを壊している状態で食べない)
        dp[i+1][1] = max(dp[i][0]+xy[i][1], dp[i][1])

print(max(dp[-1][0], dp[-1][1]))