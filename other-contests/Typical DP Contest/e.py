"""桁DP"""
d = int(input())
n = input()
l = len(n)
mod = 10**9+7

# dp[i][j][k]: i桁目まで考えて、桁の総和をdで割ったあまりがjであり、flgがk(0: 一致, 1: 真に小さい)であるときの個数
dp = [[[0]*2 for _ in range(d)] for _ in range(l+1)]
dp[0][0][0] = 1

for i in range(l):
    for j in range(d):
        for x in range(10):
            if x==int(n[i]):
                dp[i+1][(j+x)%d][0] += dp[i][j][0]
                dp[i+1][(j+x)%d][0] %= mod
            if x<int(n[i]):
                dp[i+1][(j+x)%d][1] += dp[i][j][0]
                dp[i+1][(j+x)%d][1] %= mod
            dp[i+1][(j+x)%d][1] += dp[i][j][1]
            dp[i+1][(j+x)%d][1] %= mod

print((dp[-1][0][0]+dp[-1][0][1]-1)%mod)