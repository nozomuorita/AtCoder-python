"""
・基本的にはある頂点からの最大距離+1が答えとなる
・しかし、各頂点を始点としてbfsを順次行うとO(n**2)となり、TLE
・そこで、別の方法で"木の直径"を求める
・1. ある頂点(ここでは頂点0)を始点としてbfs
・2. 頂点0からの距離が最大である頂点を始点として再びbfs
・3. このときの最大距離が木の中での直径に相当する(木の中での最大パス長)
・よって、この最大距離+1とすると答え=bfsを2回行うことで求まる
"""
from collections import deque
n = int(input())
g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
    
q = deque()
q.append(0)
dist = [-1]*n
dist[0] = 0

while q:
    v = q.popleft()
    for v2 in g[v]:
        if dist[v2]!=-1:
            continue
        dist[v2] = dist[v] + 1
        q.append(v2)
        
mx, idx = -1, -1
for i in range(len(dist)):
    if dist[i]>mx:
        mx = dist[i]
        idx = i
        
q = deque()
q.append(idx)
dist = [-1]*n
dist[idx] = 0
while q:
    v = q.popleft()
    for v2 in g[v]:
        if dist[v2]!=-1: continue
        dist[v2] = dist[v]+1
        q.append(v2)
        
ans = max(dist)
        
print(ans+1)