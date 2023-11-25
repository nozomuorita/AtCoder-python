"""BFS"""
from collections import deque
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    u, v = map(lambda x: x-1, map(int, input().split()))
    g[u].append(v)
    g[v].append(u)
    
#  辺がn-1本であるか判定
if m!=(n-1): exit(print('No'))

#  すべての頂点の次数が2以下であるか判定
for i in range(n):
    if len(g[i])>3: exit(print('No'))
    if len(g[i])==1: start=i

#  連結であるか判定
visited = [False]*n
visited[start] = True
q = deque([start])
while q:
    v = q.popleft()
    for v2 in g[v]:
        if visited[v2]: continue
        visited[v2] = True
        q.append(v2)
        
print('Yes') if all(visited) else print('No')