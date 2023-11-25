"""BFS"""
from collections import deque
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: x-1, map(int, input().split()))
    g[a].append(b)
    g[b].append(a)

visited = [False]*n
link = 0
for i in range(n):
    if visited[i]: continue
    link += 1
    q = deque([i])
    while q:
        v = q.popleft()
        visited[v] = True
        
        for v2 in g[v]:
            if visited[v2]: continue
            q.append(v2)
            
print(m-n+link)