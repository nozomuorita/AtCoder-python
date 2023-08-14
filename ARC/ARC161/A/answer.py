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
N = int(input())
A = list(map(int, input().split()))

if len(A)==1:
    print('Yes')
    exit()

A_set = set(A)
if len(A_set)==1:
    print('No')
    exit()

A.sort(reverse=True)    
num = N//2

A_big = A[:num]
A_big.sort(reverse=True)
A_small = A[num:]

for i in range(len(A_big)):
    big = A_big[i]
    if i != len(A_big)-1:
        tmp1 = A_small[i]
        tmp2 = A_small[i+1]
        
        if (tmp1 < big) and (tmp2 < big):
            continue
        else:
            print('No')
            exit()
    
    else:
        tmp1 = A_small[-1]
        big = A_big[-1]
        
        if tmp1 < big:
            continue
        else:
            print('No')
            exit()

print('Yes')