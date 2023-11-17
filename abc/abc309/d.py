from collections import deque
n, n2, m = map(int, input().split())
g = [[] for _ in range(n+n2)]
for i in range(m):
    a, b = map(lambda x: x-1, map(int, input().split()))
    g[a].append(b)
    g[b].append(a)
    
q1 = deque()
q1.append(0)
dist = [-1]*(n+n2)
dist[0] = 0

while q1:
    v = q1.popleft()
    for v2 in g[v]:
        if dist[v2]!=-1: continue
        dist[v2] = dist[v] + 1
        q1.append(v2)
        
q2 = deque()
q2.append(n+n2-1)
dist[n+n2-1] = 0

while q2:
    v = q2.popleft()
    for v2 in g[v]:
        if dist[v2]!=-1: continue
        dist[v2] = dist[v] + 1
        q2.append(v2)

ans = max(dist[:n]) + max(dist[n:]) + 1
print(ans)