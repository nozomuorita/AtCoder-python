from heapq import heapify, heappop, heappush
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b, t = map(int, input().split())
    a-=1; b-=1
    g[a].append((b, t))
    g[b].append((a, t))

ans = float("inf")
for i in range(n):
    q = [(0, i)]
    dist = [-1]*n
    dist[i] = 0
    done = [False]*n
    
    while q:
        d, v = heappop(q)
        done[v] = True
        
        for v2, t2 in g[v]:
            if dist[v2]==-1 or (dist[v]+t2<dist[v2]):
                dist[v2] = dist[v] + t2
                if done[v2]==False:
                    heappush(q, (dist[v2], v2))
    
    ans = min(ans, max(dist))

print(ans)