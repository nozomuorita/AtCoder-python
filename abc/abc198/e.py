import sys
sys.setrecursionlimit(100000000)

n = int(input())
c = list(map(int, input().split()))
g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(lambda x:x-1, map(int, input().split()))
    g[a].append(b)
    g[b].append(a)

def dfs(i):
    if color[c[i]]==0:
        ans.append(i+1)
    
    visited[i] = True
    color[c[i]] += 1
    
    for j in g[i]:
        if visited[j]: continue
        dfs(j)
    
    visited[i] = False
    color[c[i]] -= 1
    
visited = [False]*n
color = [0]*(10**5+10)
ans = []

dfs(0)
ans.sort()
for i in ans: print(i)