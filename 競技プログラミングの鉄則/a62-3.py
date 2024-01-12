"""DFS"""
import sys
sys.setrecursionlimit(100000000)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: x-1, map(int, input().split()))
    g[a].append(b)
    g[b].append(a)

ans = 0
visited = [False]*n
def dfs(v):
    visited[v] = True
    for v2 in g[v]:
        if visited[v2]: continue
        visited[v2] = True
        dfs(v2)
        
for i in range(n):
    if visited[i]: continue
    ans += 1
    dfs(i)

print("The graph is connected.") if ans==1 else print("The graph is not connected.")