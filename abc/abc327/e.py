# -*- coding: utf-8 -*-
n = int(input())
p = list(map(int, input().split()))
inf = float("inf")
dp = [[-inf]*(n+1) for _ in range(n+1)]
dp[1][0] = 0
dp[1][1] = p[0]

for i in range(1, n):
    for j in range(n+1):
        if dp[i][j]==-inf: continue

        dp[i+1][j] = max(dp[i][j], dp[i+1][j])  # 選ばないとき
        if j+1<=n:
            rate = 0.9*dp[i][j] + p[i]
            dp[i+1][j+1] = max(rate, dp[i+1][j+1])

ans = -inf
bunbo = 1
tmp = 1
for i in range(1, n+1):
    # if dp[-1][i]==-inf: continue
    rate = dp[-1][i]/bunbo - (1200/(i**0.5))
    ans = max(ans, rate)
    tmp *= 0.9
    bunbo += tmp

print(ans)
