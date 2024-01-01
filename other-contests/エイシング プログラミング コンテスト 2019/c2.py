"""DFS"""
import sys
sys.setrecursionlimit(100000000)

h, w = map(int, input().split())
s = [input() for _ in range(h)]

ans = 0
visited = [[False]*w for _ in range(h)]

def dfs(i, j):
    if s[i][j]=="#": color[0]+=1
    else: color[1]+=1
    visited[i][j] = True
    
    for d1, d2 in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        if not(0<=i+d1<h and 0<=j+d2<w): continue
        if s[i][j]==s[i+d1][j+d2]: continue
        if visited[i+d1][j+d2]: continue
        dfs(i+d1, j+d2)

for i in range(h):
    for j in range(w):
        if visited[i][j]: continue
        color = [0, 0]
        dfs(i, j)
        ans += color[0]*color[1]

print(ans)