import sys
sys.setrecursionlimit(100000000)
n, m = map(int, input().split())
g = [[] for _ in range(n)]
p = list(map(int, input().split()))
for i in range(n-1):
    g[p[i]-1].append(i+1)
    
d = [-1] * n
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    d[x] = max(d[x], y)
    
visited = [False]*n
    
def dfs(i):
    visited[i] = True
    if d[i]>0:
        for v in g[i]:
            d[v] = max(d[v], d[i]-1)
            dfs(v)

for i in range(n):
    if visited[i]==False and d[i]!=-1: dfs(i)
    
ans = 0
for i in range(n):
    if d[i]>=0: ans+=1
print(ans)