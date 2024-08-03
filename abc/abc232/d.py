from collections import deque
h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]

q = deque()
q.append((0, 0))
dist = [[-1]*w for _ in range(h)]
dist[0][0] = 1

while q:
    x, y = q.popleft()
    
    if 0<=x+1<h and c[x+1][y]=="." and dist[x+1][y]==-1:
        dist[x+1][y] = dist[x][y] + 1
        q.append((x+1, y))
    if 0<=y+1<w and c[x][y+1]=="." and dist[x][y+1]==-1:
        dist[x][y+1] = dist[x][y] + 1
        q.append((x, y+1))

ans = -1
for i in range(h):
    ans = max(ans, max(dist[i]))
print(ans)