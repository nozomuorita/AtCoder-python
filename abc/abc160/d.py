# 単純にbfs？
from collections import deque
n, x, y = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(n):
    if i==0:
        g[i].append(i+1)
    elif i==n-1:
        g[i].append(i-1)
    else:
        g[i].append(i-1)
        g[i].append(i+1)
    
x -= 1
y -= 1
g[x].append(y)
g[y].append(x)

# bfs
ans = [0] * n
for i in range(n):
    q = deque([i])
    dist = [-1] * n
    dist[i] = 0
    while q:
        v = q.popleft()
        
        for v2 in g[v]:
            if dist[v2] != -1:
                continue
            dist[v2] = dist[v] + 1
            q.append(v2)
    
    for j in range(i+ 1, n):
        if i==j: continue
        ans[dist[j]] += 1

for i in ans[1:]:
    print(i)