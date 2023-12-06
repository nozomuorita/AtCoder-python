"""ワーシャルフロイド"""
inf = float("inf")

n, m = map(int, input().split())
# dist[i][j]: iからjまで行くときのコスト(infで初期化)
dist = [[inf]*n for _ in range(n)]

#  uからvまでのコスト(直接行った場合)を書き込む
for i in range(m):
    u, v, c = map(int, input().split())
    dist[u][v] = c

#  iからiまで行くコストは0
for i in range(n):
    dist[i][i] = 0
    
#  ワーシャルフロイド
for k in range(n):
    for x in range(n):
        for y in range(n):
            dist[x][y] = min(dist[x][y], dist[x][k]+dist[k][y])

ans = 0
for i in range(n):
    for j in range(n):
        ans += dist[i][j]
print(ans)