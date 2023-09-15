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
x = list(input())
n = int(input())
s = []
for i in range(n):
    s.append(input())

# アルファベットの対応表を作る(aが新しい順番で何番目か...)
# alpha = [(aが新しい順で何番目か), (bが新しい順番で何番目か), ...]
alpha = []
for i in range(26):
    tmp = x.index(chr(ord('a')+i))
    alpha.append(tmp)

orda = ord('a')
d = defaultdict(str)

# d: 各文字列の情報を管理
# key: 文字列
# value: 各文字が新しい順で何番目かを入れたリスト
for i in range(n):
    tmp = []
    for j in s[i]:
        num = ord(j) - orda
        tmp.append(alpha[num])
    d[s[i]] = tmp

# 新しい順に対応させたリストでソート
# 小さい順で出力
d_sort = sorted(d.items(), key = lambda tmp : tmp[1])
for i in d_sort:
    print(i[0])