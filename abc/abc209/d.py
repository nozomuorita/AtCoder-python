"""
・BFSをして頂点0からの最短距離を求めておく
・c, dについてcd間の最短距離は、a-cの距離、a-d間の距離の差である
・cd間の距離が偶数なら最適な行動をとることにより町で出会う、奇数なら道で出会う
"""
from collections import deque
n, Q = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(n-1):
    a, b = map(lambda x: x-1, map(int, input().split()))
    g[a].append(b)
    g[b].append(a)
    
q = deque()
q.append(0)
dist = [-1]*n
dist[0] = 0

while q:
    v = q.popleft()
    for v2 in g[v]:
        if dist[v2]!=-1: continue
        dist[v2] = dist[v] + 1
        q.append(v2)
        
for i in range(Q):
    c, d = map(lambda x: x-1, map(int, input().split()))
    distance = max(dist[c], dist[d]) - min(dist[c], dist[d])
    
    print('Town') if distance%2==0 else print('Road')