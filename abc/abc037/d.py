"""
・heapqで実装(メモ化再帰→解説)
・まず、すべてのマスは、そのマス一つで経路とできるので初期値は1(score)
・heapqで小さいほうから見ていき、隣接するところで小さいものがあるなら、足す
・heapqの要素をタプルで(a[i][j], i, j)とするとTLE
・よって、a[i][j]に10**6、iに10**3をかけて要素とし、取り出すときに復元する
"""
from heapq import heapify, heappop, heappush
mod = 10**9+7
h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
q = []
for i in range(h):
    for j in range(w):
        heappush(q, a[i][j]*(10**6)+(i*1000)+j)
    
score = [[1]*w for _ in range(h)]
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
while q:
    cur = heappop(q)
    v = cur // (10**6)
    cur %= 10**6
    i, j = cur//1000, cur%1000
    for d1, d2 in d:
        if (0<=i+d1<h) and (0<=j+d2<w) and (a[i][j]>a[i+d1][j+d2]):
            score[i][j] += score[i+d1][j+d2]
            score[i][j] %= mod

ans = 0
for i in score: ans+=sum(i)
print(ans%mod)