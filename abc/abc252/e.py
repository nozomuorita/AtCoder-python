"""
・ダイクストラ法
・各頂点に到達する直前に使用した辺のインデックスを辞書に記録しておくことで必要な辺がわかる
"""

from heapq import heapify, heappop, heappush
from collections import defaultdict
n, m = map(int, input().split())
dic = defaultdict(int)
g = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append((b, c, i+1))
    g[b].append((a, c, i+1))
    
dist = [-1]*n
dist[0] = 0
visited = [False]*n

q = [(0, 0)]

while q:
    d, v = heappop(q)
    if visited[v]: continue
    visited[v] = True
    
    for v2, d2, idx in g[v]:
        x = d + d2
        if dist[v2]==-1 or dist[v2]>x:
            dist[v2] = x
            dic[v2] = idx
            heappush(q, (x, v2))
    
ans = set()        
for key in list(dic.keys()):
    ans.add(dic[key])
    
print(*list(ans))