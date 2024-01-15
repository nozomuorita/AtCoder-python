from collections import deque
n, x, y = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(n-1):
    u, v = map(lambda x:x-1, map(int, input().split()))
    g[u].append(v)
    g[v].append(u)

x-=1; y-=1

q = deque([x])
parent = [-1]*n
parent[x] = -100

while q:
    v = q.popleft()
    
    for v2 in g[v]:
        if parent[v2]!=-1: continue
        parent[v2] = v
        q.append(v2)

ans = []
p = y
while p!=-100:
    ans.append(p+1)
    p = parent[p]

print(*ans[::-1])