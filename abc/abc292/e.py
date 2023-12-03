from collections import deque
n, m = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    u, v = map(lambda x: x-1, map(int, input().split()))
    g[u].append(v)
    
ans = 0
for i in range(n):
    dist = [-1]*n
    q = deque([i])
    while q:
        v = q.popleft()
        for v2 in g[v]:
            if dist[v2]!=-1: continue
            dist[v2] = dist[v] + 1
            q.append(v2)
    
    for j in range(n):
        if dist[j]!=-1 and j not in g[i] and i!=j: ans+=1
    
print(ans)