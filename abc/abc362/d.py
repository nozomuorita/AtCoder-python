from collections import deque
n, m = map(int, input().split())
a = list(map(int, input().split()))
g = [[] for _ in range(n)]
for _ in range(m):
    u, v, b = map(int, input().split())
    u-=1; v-=1
    g[u].append((v, b))
    g[v].append((u, b))

q = deque()
q.append(0)
dist = [-1]*n
dist[0] = a[0]

while q:
    v = q.popleft()
    for v2, d in g[v]:
        if (dist[v2]==-1) or (dist[v2]>dist[v]+d+a[v2]):
            dist[v2] = dist[v] + d + a[v2]
            q.append(v2)

print(*dist[1:])