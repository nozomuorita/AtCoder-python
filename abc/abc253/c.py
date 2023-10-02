"""
・heapqとdefaultdictを用いて実装
・クエリ１
・個数を管理する辞書にインクリメント
・最大値と最小値を管理するheapqを作る(m1: 最小値、m2: 最大値)
・最大値はマイナスの値をpushする
・クエリ２
・辞書内で管理している個数とcを比較し、小さいほうを引く(cのほうが大きいなら集合Sでの個数は0個となる)
・クエリ３
・m1、m2(heapq)から一つずつ取り出し、辞書内で個数が0でないものが出現するまで取り出す(while文)
・初めて個数が0でないものが出現したらそれが最大値、最小値なので差を計算して出力
"""

from collections import defaultdict
from heapq import heapify, heappop, heappush

d = defaultdict(int)
m1 = []
m2 = []

q = int(input())
for i in range(q):
    query = list(map(int, input().split()))
    if query[0]==1:
        x = query[1]
        d[x] += 1
        heappush(m1, x)
        heappush(m2, -x)
        
    elif query[0]==2:
        x = query[1]
        c = query[2]
        
        mn = min(c, d[x])
        d[x] -= mn
        
    else:
        while 1:
            mn = heappop(m1)
            if d[mn] != 0:
                heappush(m1, mn)
                break
        while 1:
            mx = heappop(m2)
            if d[-mx] != 0:
                heappush(m2, mx)
                mx = -mx
                break
        print(mx - mn)