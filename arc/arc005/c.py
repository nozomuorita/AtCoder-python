"""01-BFS"""
from collections import deque
h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if c[i][j]=="s": sx, sy=i, j
        if c[i][j]=="g":
            gx, gy=i, j
            c[i][j] = "."

dist = [[-1]*w for _ in range(h)]
dist[sx][sy] = 0
q = deque()
q.append((sx, sy))

while q:
    x, y = q.popleft()
    
    for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if 0<=x+i<h and 0<=y+j<w:
            if dist[x+i][y+j]!=-1: continue
            if c[x+i][y+j]==".":
                dist[x+i][y+j] = dist[x][y]
                q.appendleft((x+i, y+j))
            elif c[x+i][y+j]=="#":
                dist[x+i][y+j] = dist[x][y]+1
                q.append((x+i, y+j))

print("YES") if dist[gx][gy]<=2 else print("NO")