"""BFS"""
from collections import deque
n, m = map(int, input().split())
g = [[] for _ in range(n)]
ab = []
for i in range(m):
    a, b = map(lambda x:x-1, map(int, input().split()))
    g[a].append(b)
    g[b].append(a)
    ab.append([a, b])

ans = 0
for i in range(m):
    q = deque([0])
    used = [False]*n
    used[0] = True
    
    while q:
        v = q.popleft()
        
        for v2 in g[v]:
            if used[v2]: continue
            if [min(v, v2), max(v, v2)]==ab[i]: continue
            used[v2] = True
            q.append(v2)
    
    if not(all(used)): ans+=1
    
print(ans)