h, n = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

inf = float('inf')

#  dp[i][j]: i番目までの魔法を使って、モンスターの残りの体力がjであるときの最小魔力
dp = [[inf]*(h+1) for _ in range(n+1)]
dp[0][h] = 0                                    #  初期値: 魔法を使わないで、モンスターの体力がhであるときの使用魔力は0(dp[0][h-2]などは実現不可能なのでinfとする)

for i in range(n):
    a, b = ab[i][0], ab[i][1]
    for j in range(h, -1, -1):
        # 魔法を使わない
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        # 魔法を使う
        dp[i+1][max(0, j-a)] = min(dp[i+1][max(0, j-a)], dp[i+1][j]+b)  #  魔法を使うなら、魔法を使った場合と使わない場合で最小魔力を比較
        
print(dp[-1][0])