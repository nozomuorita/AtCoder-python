import heapq

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    u, v, c = map(int, input().split())
    g[u].append((v, c))
    
q = []
heapq.heappush(q, (0, 0))
dist = [-1] * n
dist[0] = 0
done = [False] * n

while q:
    i, j = heapq.heappop(q)
    
    if done[j]:
        continue
    done[j] = True
    for k in g[j]:
        if (dist[k[0]]==-1) or (dist[k[0]]>dist[j]+k[1]):
            dist[k[0]] = dist[j] + k[1]
            heapq.heappush(q, (dist[k[0]], k[0]))
            
print(dist[-1])