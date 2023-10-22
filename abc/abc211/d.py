from collections import defaultdict, deque
mod = 10**9+7
n, m = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(lambda x: x-1, map(int, input().split()))
    g[a].append(b)
    g[b].append(a)
    
q = deque()
q.append(0)
dist = [-1]*n
dist[0] = 0
ans = [0]*n
ans[0] = 1

while q:
    v = q.popleft()
    for v2 in g[v]:
        if dist[v2]!=-1:
            if dist[v2]==dist[v]+1:
                ans[v2] += ans[v]
                ans[v2] %= mod
        else:
            dist[v2] = dist[v] + 1
            ans[v2] = ans[v]
            ans[v2] %= mod
            q.append(v2)
        
print(ans[-1]%mod)