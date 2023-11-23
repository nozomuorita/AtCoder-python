import sys
sys.setrecursionlimit(100000000)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    u, v = map(lambda x: x-1, map(int, input().split()))
    g[u].append(v)
    g[v].append(u)
    
ans = 1
visited = [True] + ([False]*(n-1))
    
def dfs(i, vis):
    global ans
    if ans>=10**6: exit(print(10**6))
    for v in g[i]:
        if vis[v]: continue
        
        ans += 1
        
        vis[v] = True
        dfs(v, vis)
        vis[v] = False
        
dfs(0, visited)
print(ans)