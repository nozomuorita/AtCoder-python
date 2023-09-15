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
n, q = map(int, input().split())
boll = [i for i in range(n)] # 0~n-1までの数字が書かれたボール
idx = [i for i in range(n)] # 各ボールのインデックス番号

for i in range(q):
    x = int(input())
    x -= 1
    # x_idx: xと書かれたボールがある場所
    x_idx = idx[x]

    # x_idxが(n-1)(右端)でないならば、
    if x_idx != n-1:
        tmp = boll[x_idx+1]
        boll[x_idx], boll[x_idx+1] = boll[x_idx+1], boll[x_idx]
        idx[x] += 1
        idx[tmp] -= 1
    # x_idxが右端ならば
    else:
        # ボールを交換
        tmp = boll[x_idx-1]
        boll[x_idx-1], boll[x_idx] = boll[x_idx], boll[x_idx-1]
        # インデックス番号も更新
        idx[x] -= 1
        idx[tmp] += 1

for i in range(n):
    boll[i] += 1

print(*boll)