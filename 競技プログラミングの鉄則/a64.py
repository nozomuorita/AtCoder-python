"""ダイクストラ法"""
from heapq import heapify, heappop, heappush
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    a-=1; b-=1
    g[a].append((b, c))
    g[b].append((a, c))

q = [(0, 0)]
dist = [-1]*n
dist[0] = 0
done = [False]*n

while q:
    d, v = heappop(q)
    if done[v]: continue
    done[v] = True
    
    for v2, d2 in g[v]:
        if dist[v2]==-1 or dist[v2]>dist[v]+d2:
            dist[v2] = dist[v] + d2
            heappush(q, (dist[v2], v2))
        
for i in range(n): print(dist[i])