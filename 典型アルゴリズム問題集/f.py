"""最小全域木(プリム法)"""
from heapq import heapify, heappop, heappush
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    u, v, c = map(int, input().split())
    g[u].append((v, c))
    g[v].append((u, c))
    
marked = [False]*n
marked[0] = True
marked_count = 1

q = []
for v, c in g[0]: heappush(q, (c, v))

ans = 0
while marked_count<n:
    c, v = heappop(q)
    if marked[v]: continue
    
    marked[v] = True
    marked_count += 1
    ans += c
    
    for v2, c2 in g[v]:
        if marked[v2]: continue
        heappush(q, (c2, v2))

print(ans)