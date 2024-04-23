"""
・解説とは違う解法
・頂点1を色0とし、距離0(始点)とする
・bfsで探索し、頂点1からの距離が偶数なら頂点1と同じ色(0)に塗る
・奇数なら逆の色で塗る
"""

from collections import deque
n = int(input())
g = [[] for _ in range(n)]
for i in range(n-1):
    u, v, w = map(int, input().split())
    u-=1; v-=1
    g[u].append((v, w))
    g[v].append((u, w))

color = [-1]*n
color[0] = 0
dist = [-1]*n
dist[0] = 0
done = [False]*n
q = deque([0])

while q:
    v = q.popleft()
    if done[v]: continue
    done[v] = True
    
    for v2, d in g[v]:
        if dist[v2]!=-1: continue
        dist[v2] = dist[v] + d
        if dist[v2]%2==0:
            color[v2] = 0
        else:
            color[v2] = 1
        q.append(v2)

for i in color:
    print(i)