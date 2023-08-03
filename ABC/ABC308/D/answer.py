# @nzm_ort
# https://github.com/nozomuorita/atcoder-workspace-python

# import module ------------------------------------------------------------------------------
from collections import defaultdict, deque, Counter
import math
from itertools import combinations, permutations, product, accumulate, groupby, chain
from heapq import heapify, heappop, heappush
import bisect
import sys
sys.setrecursionlimit(100000000)
inf = float('inf')
mod1 = 10**9+7
mod2 = 998244353
def ceil_div(x, y): return -(-x//y) # 切り上げ

# main code ------------------------------------------------------------------------------------
h, w = map(int, input().split())
s = [input() for _ in range(h)]

snuke = 'snuke'
visited = [[False]*w for _ in range(h)]

def dfs(i, j, n):
    visited[i][j] = True
    if (i==h-1) and (j==w-1):
        if s[i][j]==snuke[n]:
            print('Yes')
            exit()

    else:
        if s[i][j] == snuke[n]:
            for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if (0<=i2<h) and (0<=j2<w):
                    if (s[i2][j2]==snuke[(n+1)%5]) and (not(visited[i2][j2])):
                        dfs(i2, j2, (n+1)%5)

dfs(0, 0, 0)

print('No')