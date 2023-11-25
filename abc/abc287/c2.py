"""DFS"""
import sys
sys.setrecursionlimit(100000000)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    u, v = map(lambda x: x-1, map(int, input().split()))
    g[u].append(v)
    g[v].append(u)
    
#  辺がn-1本であるか判定
if m!=(n-1): exit(print('No'))

#  すべての頂点の次数が2以下であるか判定
for i in range(n):
    if len(g[i])>3: exit(print('No'))
    if len(g[i])==1: start=i
    
#  グラフが連結であるか判定
visited = [False]*n
visited[start] = True
def dfs(i):
    for v in g[i]:
        if visited[v]: continue
        visited[v] = True
        dfs(v)

dfs(start)

print('Yes') if all(visited) else print('No')