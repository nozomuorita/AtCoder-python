"""
・BFSで遷移
・たどり着けるなら距離(=最短回数)を出力
・愚直シミュレーションでもいけるっぽい
"""
from collections import deque
n = int(input())
g = [[] for _ in range(n)]

for i in range(n):
    a = int(input()) - 1
    g[i].append(a)
    
q = deque([0])
dist = [-1]*n
dist[0] = 0

while q:
    v = q.popleft()
    
    for v2 in g[v]:
        if dist[v2]!=-1: continue
        if v2==v: continue
        dist[v2] = dist[v]+1
        q.append(v2)
        
print(dist[1]) if dist[1]!=-1 else print(-1)