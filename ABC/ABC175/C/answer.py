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
x, k, d = map(int, input().split())

# xがマイナスの時は、すべての動きが反転したものと考え、一般性を失わずabs(x)とする
x = abs(x)

# m: 0に最も近いところまで、移動するのに必要な移動回数
m = x//d
# mがk(移動回数)よりも小さいなら、ひとまず0に最も近いところまで移動し、x(移動後の座標)とk(残りの移動回数)を更新
if m < k:
    x -= m * d
    k -= m
# mがk(移動回数)よりも大きい → k回の移動で、最も0に近いところまで移動することはできない
# k回だけ、0の方向へできる限り(k回)移動したものが答え
else:
    ans = abs(x) - (k*d)
    print(ans)
    exit()

# 残りの移動回数が偶数なら今いる最も0に近い座標が答え
if k%2==0:
    print(abs(x))
# 奇数なら、今いる最も0に近い座標から一回分移動した座標が答え
else:
    ans = min(abs(x-d), abs(x+d))
    print(ans)