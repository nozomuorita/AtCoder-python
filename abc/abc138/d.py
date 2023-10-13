"""
・各pにいくら足したのかを辞書でカウントする
・各pに足したxはそれ以下の子頂点にすべて反映されることになる
・よってbfsでたどっていき、頂点1から順に足していくことで、各頂点の値が求まる
"""

from collections import defaultdict, deque

n, q = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(lambda x: x-1, map(int, input().split()))
    g[a].append(b)
    g[b].append(a)
    
c = defaultdict(int)
for i in range(q):
    p, x = map(int, input().split())
    c[p-1] += x                            # p-1を根とした部分木の各頂点にはxをたす
    
q = deque()
q.append(0)
dist = [-1]*n
dist[0] = c[0]

while q:
    v = q.popleft()
    
    for v2 in g[v]:
        if dist[v2]!=-1: continue
        dist[v2] = dist[v] + c[v2]
        q.append(v2)
        
print(*dist)