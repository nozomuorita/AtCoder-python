import sys
sys.setrecursionlimit(100000000)
n, x, y = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(lambda x:x-1, map(int, input().split()))
    g[a].append(b)
    g[b].append(a)

x-=1; y-=1

def dfs(pos):
    visited[pos] = True
    ans.append(pos)
    
    if pos==y:
        for i in ans: print(i+1, end=" ")
        exit()
    
    for v in g[pos]:
        if visited[v]: continue
        dfs(v)
    ans.pop()
    
ans = []
visited = [False] * n
dfs(x)