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
n, m = map(int, input().split())
a = []
for i in range(2*n):
    _ = input()
    a.append(_)

# 1: oneの勝ち
# 0: あいこ
# -1: twoの勝ち
def janken(one, two):
    if (one=='G'):
        if (two=='G'):
            return 0
        elif (two=='C'):
            return 1
        else:
            return -1
    elif (one=='C'):
        if (two=='G'):
            return -1
        elif (two=='C'):
            return 0
        else:
            return 1
    else:
        if (two=='G'):
            return 1
        elif (two=='C'):
            return -1
        else:
            return 0

# ex_win: 勝ち以外(あいこか負け)であった回数(小さいほど勝ち回数が多い)
ex_win = []
for i in range(2*n):
    ex_win.append([0, i])

# print(f'ex_win: {ex_win}')
# print(f'a: {a}')

for i in range(m):
    for j in range(n):
        # (2*j)番目と(2*j+1)番目がじゃんけん
        one = ex_win[2*j][1] # 2*j番目の人の番号
        two = ex_win[2*j+1][1] # 2*j+1番目の人の番号
        one_p = a[one][i] # 2*j番目の人の出す手
        two_p = a[two][i] # 2*j+1番目の人の出す手
        # print(one, one_p, two, two_p)

        result = janken(one_p, two_p)
        # print(result)
        # じゃんけんの結果が1(oneの勝ち)ならtwoに1足す(負け分)
        if result == 1:
            ex_win[2*j+1][0] += 1
        elif result == -1:
            ex_win[2*j][0] += 1
        else:
            ex_win[2*j][0] += 1
            ex_win[2*j+1][0] += 1

    ex_win.sort()
#     print(f'sorted: {ex_win}')
# print('-----------')
for i in range(len(ex_win)):
    print(ex_win[i][1]+1)