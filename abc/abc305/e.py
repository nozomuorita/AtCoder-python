"""解説参考"""
from heapq import heapify, heappop, heappush
n, m, k = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: x-1, map(int, input().split()))
    g[a].append(b)
    g[b].append(a)

d = [-1]*n    # 各頂点にたどり着いた警備員の体力の最大値
hq = []
for i in range(k):
    p, h = map(int, input().split())
    p -= 1
    d[p] = h                   # 最初に警備員がいる頂点は体力h
    heappush(hq, (-h, p))      # heapqに追加→(-体力, 頂点番号)

ok = [False]*n                 # 各頂点において、警備員の最大体力が確定しているかどうか
# heapqが空でない間繰り返す
while hq:
    h, p = heappop(hq)
    h *= (-1)                  # 体力を正に戻す
    
    if ok[p]: continue         # もし、確定済みならcontinue
    ok[p] = True               # 確定していないなら、頂点pを確定する
    if d[p]==0: continue       # もし、pの最大体力が0なら、以降の処理はしない(移動できないので)
    
    for p2 in g[p]:
        if ok[p2]: continue                 # p2が確定済みならcontinue
        d[p2] = max(d[p2], d[p]-1)          # d[p2]を更新
        heappush(hq, (-d[p2], p2))          # heapqに追加

ans1, ans2 = 0, []
for i in range(n):
    if d[i]!=-1:
        ans1 += 1
        ans2.append(i+1)

print(ans1)
print(*ans2)