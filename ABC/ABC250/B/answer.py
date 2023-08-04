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

ans = []
f = True

for i in range(n*a):
    tmp = ''
    for j in range(n*b):
        if f:
            if (i//a)%2==0:
                if (j//b)%2==0:
                    tmp += '.'
                else:
                    tmp += '#'
            else:
                if (j//b)%2==0:
                    tmp += '.'
                else:
                    tmp += '#'
                    
        else:
            if (i//a)%2==0:
                if (j//b)%2==0:
                    tmp += '#'
                else:
                    tmp += '.'
            else:
                if (j//b)%2==0:
                    tmp += '#'
                else:
                    tmp += '.'
            
    ans.append(tmp)
    if i%a==a-1:
        f = not(f)

for i in ans:
    print(i)