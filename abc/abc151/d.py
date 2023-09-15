"""
・BFS
・各マス(i, j)についてBFSをする
・求めた各距離は(i, j)からの最小距離である
・求めた距離の中で最大のものを取り出すと、それは(i, j)を始点とした場合の最小距離の最大値である
・ansより大きいなら更新
"""

from collections import deque
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

ans = -1
for sx in range(h):
    for sy in range(w):
        if s[sx][sy]=='#':
            continue
        q = deque()
        q.append((sx, sy))
        dist = [[-1]*w for _ in range(h)]
        dist[sx][sy] = 0
        
        while q:
            i, j = q.popleft()
            for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if not(0<=i2<h) or not(0<=j2<w):
                    continue
                if s[i2][j2]=='#':
                    continue
                if dist[i2][j2] != -1:
                    continue
                dist[i2][j2] = dist[i][j] + 1
                q.append((i2, j2))
        
        mx = max(list(map(lambda x: max(x), dist)))
        if mx > ans:
            ans = mx
            
print(ans)