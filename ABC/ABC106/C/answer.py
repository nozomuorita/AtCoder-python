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
s = list(input())
k = int(input())

# 2以上の場合、5000兆日後には、必ずkの範囲を超えた文字数になる
# したがって、2以上の値が出てきたらそれが答え
n = 0
for i in s:
    if i in '23456789':
        print(i)
        break
    else:
        n += 1
        if n == k:
            print(1)
            break


# n = 0
# day = 5 * (10**15)
# for i in s:
#     print(i)
#     i = int(i)
#     #n += i ** day
#     n += pow_r(i, day)
#     print(n)
    
#     if n >= k:
#         print(i)
#         break