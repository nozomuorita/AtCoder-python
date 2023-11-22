""" DFS """
import sys
sys.setrecursionlimit(100000000)
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    u, v = map(lambda x: x-1, map(int, input().split()))
    g[u].append(v)
    g[v].append(u)
    
visited = [False]*n
def dfs(i):
    for v in g[i]:
        if not(visited[v]):
            visited[v] = True
            dfs(v)
        
ans = 0
for i in range(n):
    if not(visited[i]):
        ans += 1
        dfs(i)
        
print(ans)