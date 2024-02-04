"""桁DP"""
n = input()

# dp[i][j][k]: i桁目まで考えて、flgがk(0: 一致, 1: 未満)のとき、桁和をjとできるか
dp = [[[0]*2 for _ in range(9*len(n)+10)] for _ in range(len(n)+1)]
dp[0][0][0] = 1

for i in range(len(n)):
    for j in range(9*len(n)):
        for x in range(10):
            if x==int(n[i]):
                dp[i+1][j+x][0] += dp[i][j][0]
            if x<int(n[i]):
                dp[i+1][j+x][1] += dp[i][j][0]
            dp[i+1][j+x][1] += dp[i][j][1]

for i in range(9*len(n), -1, -1):
    if dp[-1][i][0]!=0 or dp[-1][i][1]!=0:
        exit(print(i))