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
n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())

ans = [[] for _ in range(p, q+1)]
print(ans)

for i in range(p, q+1):
    ans = []
    for j in range(r, s+1):
        if ((i+j)==(a+b)) or ((i-j)==(a-b)):
            ans.append('#')
        else:
            ans.append('.')

    print(''.join(ans))