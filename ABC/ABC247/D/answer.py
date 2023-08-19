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
q = int(input())
# 現在の筒の中の状態をランレングス符号化で管理(厳密ではない)
# ex: 2が3個、3が4個入っているとき→boll=[(2, 3), (3, 4)]
boll = deque() 

for i in range(q):
    query = list(map(int, input().split()))
    # クエリ1なら、キューに追加(ランレングス符号化方式で)
    if query[0] == 1:
        x = query[1]
        c = query[2]
        boll.append((x, c))
    # クエリ2ならキューから順に取り出していく
    else:
        c = query[1]
        ans = 0
        while 1:
            b = boll.popleft()
            # とりだしたボールの数がcよりも多いなら → c個分だけ取り出して和を出力 → 取り出したc個分を引いた値を再びキューへ(左側挿入)
            if b[1]>=c:
                ans += b[0]*c
                print(ans)
                if b[1]>c:
                    boll.appendleft(((b[0], b[1]-c)))
                break
            # 取り出したボールの数がcよりも少ないなら、ansに追加してさらに取り出す(popleft)
            else:
                ans += b[0]*b[1]
                c -= b[1]