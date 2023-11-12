"""
・二部グラフ判定
"""
from collections import defaultdict, deque
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

g = [set() for _ in range(n)]
for i in range(m):
    g[a[i]-1].add(b[i]-1)
    g[b[i]-1].add(a[i]-1)
    
x = [-1]*n
for i in range(n):
    if x[i]!=-1: continue
    q = deque([i])
    while q:
        v = q.popleft()
        if v==-1: x[v]=0
        for v2 in g[v]:
            if x[v2]==-1: x[v2]=int(not(x[v])); q.append(v2)
            else:
                if x[v]==x[v2]: exit(print('No'))
                
print('Yes')