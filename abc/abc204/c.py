"""
・各頂点を始点としてDFSをして、到達できるかどうかを判定
"""
import sys
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)

def dfs(i):
    for j in g[i]:
        if visited[j]: continue
        visited[j] = True
        dfs(j)

ans = 0
for i in range(n):
    visited = [False]*n
    visited[i] = True
    dfs(i)
    ans += visited.count(True)

print(ans)