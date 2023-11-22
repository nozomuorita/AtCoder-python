"""BFS"""
from collections import deque
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    u, v = map(lambda x: x-1, map(int, input().split()))
    g[u].append(v)
    g[v].append(u)
    
ans = 0
    
visited = [False]*n
for i in range(n):
    if not(visited[i]):
        ans += 1
        q = deque([i])
        while q:
            v = q.popleft()
            for v2 in g[v]:
                if visited[v2]: continue
                visited[v2] = True
                q.append(v2)
                
print(ans)