"""
・スタートからゴールまでの最短経路のみ白ければ良い
・それ以外は黒くするのが最適
・到達できないなら-1
"""
from collections import deque
h, w = map(int, input().split())
s = [input() for _ in range(h)]

if s[0][0]!="." or s[-1][-1]!=".": exit(print(-1))

q = deque([[0, 0]])
dist = [[-1]*w for _ in range(h)]
dist[0][0] = 0
while q:
    i, j = q.popleft()
    
    for d1, d2 in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if (0<=i+d1<h) and (0<=(j+d2)<w) and dist[i+d1][j+d2]==-1:
            if s[i+d1][j+d2]==".":
                dist[i+d1][j+d2] = dist[i][j] + 1
                q.append([i+d1, j+d2])
    
if dist[-1][-1]==-1: exit(print(-1))

black = 0
for i in range(h):
    for j in range(w):
        if s[i][j]=="#": black+=1
ans = (h*w) - (dist[-1][-1]+1) - black
print(ans)