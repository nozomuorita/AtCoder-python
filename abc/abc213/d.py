import sys
sys.setrecursionlimit(100000000)

n = int(input())
g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(lambda x: x-1, map(int, input().split()))
    g[a].append(b)
    g[b].append(a)

route = []
visited = [False]*n
visited[0] = True
def dfs(i):
    for j in sorted(g[i]):
        route.append(i+1)
        if visited[j]: continue
        visited[j] = True
        dfs(j)
        route.append(j+1)

dfs(0)
ans = [route[0]]
for i in range(1, len(route)):
    if route[i]!=route[i-1]: ans.append(route[i])
ans.append(1)
print(*ans)