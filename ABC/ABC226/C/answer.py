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
T = []
K = []
A = []
# g[i]: 技iを習得するために必要な技(0-index)
g = [[] for _  in range(n)] # 隣接リスト

for i in range(n):
    tka = list(map(int, input().split()))
    T.append(tka[0])
    K.append(tka[1])
    A.append(tka[2:])
    for j in tka[2:]:
        if j==0:
            continue
        else:
            g[i].append(j-1)

# キューに技Nの習得に必要な技番号を入れる
# q: 習得する必要のある技を順次入れていく
q = deque()
for i in g[-1]:
    q.append(i)

# clear[i]: 技iを習得したかどうか
clear = [False] * n
# 答え: 必要な時間(技Nは最初に見ているため、あらかじめ技Nの習得に必要な時間を入れる)
ans = T[-1]

# BFS
# キューから一つずつ取り出し、以下の処理を行う
# すでに習得済み(clear[num]==True)なら何もせず続ける
# 習得済みでない場合、その技を習得する(clear[num]をTrueに、ansに技numの習得に必要な時間を足す)
# 技numの習得に必要な技をキューに追加(その技がすでに習得済みならキューには入れない)
# いずれ(技1に到達すると)習得する必要のある技がなくなるので、キューが空になり操作が終了する
while q:
    num = q.popleft()
    if clear[num]:
        continue
    else:
        clear[num] = True
        ans += T[num]
        for i in g[num]:
            if clear[i]:
                continue
            else:
                q.append(i)

print(ans)