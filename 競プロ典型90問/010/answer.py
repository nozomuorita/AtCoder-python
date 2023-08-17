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
one = [0] # 累積和
two = [0]

for i in range(n):
    c, p = map(int, input().split())
    if c==1:
        one.append(one[-1]+p)
        two.append(two[-1])
    else:
        one.append(one[-1])
        two.append(two[-1]+p)

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    ans_one = one[r] - one[l-1]
    ans_two = two[r] - two[l-1]
    print(ans_one, ans_two)