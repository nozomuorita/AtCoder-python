"""桁DP"""
N = input()
K = int(input())

# dp[i][j][k]: i桁目まで考えて、0でない数字がj個あり、flgがk(0: 一致, 1: 未満)であるときの個数
dp = [[[0]*2 for _ in range(K+1)] for _ in range(len(N)+1)]
dp[0][0][0] = 1

for i in range(len(N)):
    for j in range(K+1):
        for x in range(10):
            if x==int(N[i]):
                if x==0:
                    dp[i+1][j][0] += dp[i][j][0]
                else:
                    if j+1<=K: dp[i+1][j+1][0] += dp[i][j][0]
            if x<int(N[i]):
                if x==0:
                    dp[i+1][j][1] += dp[i][j][0]
                else:
                    if j+1<=K: dp[i+1][j+1][1] += dp[i][j][0]
            if x==0:
                dp[i+1][j][1] += dp[i][j][1]
            else:
                if j+1<=K: dp[i+1][j+1][1] += dp[i][j][1]

print(dp[-1][K][0]+dp[-1][K][1])