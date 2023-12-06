"""ワーシャルフロイド"""
h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
a = [list(map(int, input().split())) for _ in range(h)]

inf = float("inf")
dist = [[inf]*10 for _ in range(10)]

for i in range(10):
    for j in range(10):
        dist[i][j] = c[i][j]

for k in range(10):
    for x in range(10):
        for y in range(10):
            dist[x][y] = min(dist[x][y], dist[x][k]+dist[k][y])

ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j]==-1: continue
        ans += dist[a[i][j]][1]
print(ans)