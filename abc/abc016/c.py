from collections import deque
n, m = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(lambda x: x-1, map(int, input().split()))
    g[a].append(b)
    g[b].append(a)
    
ans = []
for i in range(n):
    q = deque([i])
    dist = [-1]*n
    dist[i] = 0
    
    while q:
        v = q.popleft()
        
        for v2 in g[v]:
            if dist[v2]==-1:
                dist[v2] = dist[v] + 1
                q.append(v2)
    
    ans.append(dist.count(2))

for i in range(n): print(ans[i])