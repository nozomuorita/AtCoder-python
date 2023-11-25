"""DFS"""
"""連結成分の大きさを調べる(解説)"""
import sys
sys.setrecursionlimit(100000000)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: x-1, map(int, input().split()))
    g[a].append(b)
    g[b].append(a)

link = 0             #  連結成分の個数
def dfs(i):
    used[i] = True
    
    for v in g[i]:
        if used[v]: continue
        dfs(v)

used = [False]*n
for i in range(n):
    if used[i]: continue
    link += 1
    dfs(i)
    
print(m-n+link)