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
s = input()

# 連続しているものが対象となる、連続している数をaとしてa_C_2をすべて足したものが答え
sequence = []
tmp = 1
for i in range(1, n):
    if s[i]==s[i-1]:
        tmp += 1
        if i==(n-1):
            sequence.append(tmp)
    else:
        if tmp >= 2:
            sequence.append(tmp)
        tmp = 1

ans = 0
for i in sequence:
    ans += int((i*(i-1)) / 2)

print(ans)