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

#  持っているsをすべて使い切ることができないか、持っているsをすべて使ったあと、残りのcでsccを作ることができない場合
#  持っているcでできる限り作ったものが答え
if n >= m//2:
    ans = m//2
#  sをすべて使ったあと、余ったcからsccを作れる場合
else:
    ans = n
    m -= 2*n
    n -= n
    ans += m//4

print(ans)