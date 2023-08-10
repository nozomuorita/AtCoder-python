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
n = int(input())

ans = ''

while (n != 0):
    s = n % 26
    s -= 1
    # 余りが0の場合はzである
    if s == -1:
        ans += 'z'
        # 26を引かないと、n//=26をしたときに１大きくなってしまう
        n -= 26
    else:
        # chr(97)='a'である
        ans += chr(97+s)
        # 処理を共通化するために、記述。なくても問題はない
        n -= n%26

    n //= 26

# 逆順で出力
print(ans[: : -1])