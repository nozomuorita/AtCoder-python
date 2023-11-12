n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j]: i品目まで食べたときのおなかの状態がjのときの最大値(0: 壊していない、1: 壊している)
dp = [[0, 0] for _ in range(n+1)]

for i in range(n):
    x, y = xy[i][0], xy[i][1]
    if x==0:
        dp[i+1][0] = max(dp[i][0]+y, dp[i][1]+y, dp[i][0])
        dp[i+1][1] = dp[i][1]
    else:
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = max(dp[i][0]+y, dp[i][1])
        
print(max(dp[-1][0], dp[-1][1]))