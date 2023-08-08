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
a, b, k, l = map(int, input().split())

# セット売りみかんの1つあたりの値段と一つ売りのみかんの値段を比較し、金額の小さいほうを多く買う
if a <= (b/l):
    ans = a*k
else:
    # k個以上なので、セット売りですべて買うか、あまり分だけばら売りを買うかで小さいほうを答えとする
    ans1 = (k//l)*b + (k%l)*a
    ans2 = (ceil_div(k, l))*b
    ans = min(ans1, ans2)

print(ans)