from collections import deque
h, w = map(int, input().split())
sx, sy = map(lambda x:x-1, map(int, input().split()))
gx, gy = map(lambda x:x-1, map(int, input().split()))
s = [input() for _ in range(h)]

dist = [[[1<<60]*4 for i in range(w)] for j in range(h)]
dist[sx][sy] = [0]*4

# 0: 上, 1: 右, 2: 下, 3: 左
q = deque()
for i in range(4): q.append((sx, sy, i))

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

while q:
    x, y, k = q.popleft()
    
    for i in range(4):
        d1, d2, k2 = dx[i], dy[i], i
        if x+d1<0 or h<=x+d1 or y+d2<0 or w<=y+d2: continue
        if s[x+d1][y+d2]=="#": continue

        score=0 if k==k2 else 1
        d = dist[x][y][k] + score
        
        if d<dist[x+d1][y+d2][k2]:
            dist[x+d1][y+d2][k2] = d
            if k==k2: q.appendleft((x+d1, y+d2, k2))
            else: q.append((x+d1, y+d2, k2))
            
print(min(dist[gx][gy]))