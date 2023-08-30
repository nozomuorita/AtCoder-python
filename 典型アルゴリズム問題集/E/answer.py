inf = float('inf')

n, m = map(int, input().split())
dist = [[inf]*n for _ in range(n)]  # dist[i][j]: iからjまでの最短距離(初期値をinfとする)
for i in range(m):
    u, v, c = map(int, input().split())
    dist[u][v] = c
    
# 同じ頂点同士の距離を0とする
for i in range(n):
    dist[i][i] = 0
    
# ワーシャルフロイド法
for k in range(n):
    for x in range(n):
        for y in range(n):
            dist[x][y] = min(dist[x][y], dist[x][k]+dist[k][y])
            
# すべての頂点について最短距離を足す
ans = 0
for i in range(n):
    for j in range(n):
        ans += dist[i][j]
        
print(ans)