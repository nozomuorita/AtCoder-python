from collections import deque
h, w = map(int, input().split())
c = [input() for _ in range(h)]

for i in range(h):
    for j in range(w):
        if c[i][j]=="S": sx, sy=i, j

for d1, d2 in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
    if sx+d1<0 or sx+d1>=h or sy+d2<0 or sy+d2>=w or c[sx+d1][sy+d2]=="#": continue

    q = deque()
    q.append((sx+d1, sy+d2))
    dist = [[-1]*w for _ in range(h)]
    dist[sx+d1][sy+d2] = 1
    
    while q:
        vx, vy = q.popleft()
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=(vx+dx)<h and 0<=(vy+dy)<w:
                if c[vx+dx][vy+dy]=="#": continue
                if dist[vx+dx][vy+dy]!=-1 or (vx+dx==sx and vy+dy==sy): continue
                dist[vx+dx][vy+dy] = dist[vx][vy] + 1
                q.append((vx+dx, vy+dy))

    for tx, ty in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if [tx, ty]==[d1, d2]: continue
        if sx+tx<0 or sx+tx>=h or sy+ty<0 or sy+ty>=w: continue
        if dist[sx+tx][sy+ty]!=-1: exit(print("Yes"))
        
print("No")    