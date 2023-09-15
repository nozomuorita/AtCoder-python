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
s = input()
list_ = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

for i in range(len(list_)):
    if list_[i]==s:
        n = i
        break
        
print(7-int((n%7)))