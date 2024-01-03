from collections import deque
h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if a[i][j]=="S": sx, sy=i, j
        elif a[i][j]=="G": gx, gy=i, j
        elif a[i][j]=="<":
            x = j-1
            while x>=0:
                if a[i][x]=="." or a[i][x]=="$": a[i][x]="$"
                else: break
                x -= 1
        elif a[i][j]==">":
            x = j+1
            while x<w:
                if a[i][x]=="." or a[i][x]=="$": a[i][x]="$"
                else: break
                x += 1
        elif a[i][j]=="^":
            y = i-1
            while y>=0:
                if a[y][j]=="." or a[y][j]=="$": a[y][j]="$"
                else: break
                y -= 1
        elif a[i][j]=="v":
            y = i+1
            while y<h:
                if a[y][j]=="." or a[y][j]=="$": a[y][j]="$"
                else: break
                y += 1

q = deque()
q.append((sx, sy))
dist = [[-1]*w for _ in range(h)]
dist[sx][sy] = 0

while q:
    x, y = q.popleft()
    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0<=(x+dx)<h and 0<=(y+dy)<w:
            if dist[x+dx][y+dy]!=-1: continue
            if a[x+dx][y+dy]=="." or a[x+dx][y+dy]=="G":
                dist[x+dx][y+dy] = dist[x][y] + 1
                q.append((x+dx, y+dy))

print(dist[gx][gy])