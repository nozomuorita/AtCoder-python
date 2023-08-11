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
# 自力AC
a, b, x = map(int, input().split())

# 最小の整数１を満たすか確認
if (a+b>x):
    print(0)
    exit()
# 売られている最大の整数の金額よりもxが大きいならば、最大値(10**9)で出力
if ((a*(10**9))+(b*10) < x):
    print(10**9)
    exit()

# 桁数を求める
length = 1
m = 1
while (a*(m)+b*length <= x):
    length += 1
    m *= 10

length -= 1

# 二分探索
left = 10**(length-1)
right = 10**(length) - 1

while (left <= right):
    mid = (left + right) // 2
    mid_value = (a*mid) + (b*(length))

    if x == mid_value:
        print(mid)
        exit()
    if x < mid_value:
        right = mid - 1
    if x > mid_value:
        left = mid + 1

# leftとrightの間のどれかが境界であるため、あとはfor文で調べる
mn = min(left, right)
mx = max(left, right)
for i in range(mn, mx+1):
    money = (a*i)+(b*length)
    if money > x:
        break

print(i-1)