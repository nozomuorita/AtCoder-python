mod = 998244353
n, m, k = map(int, input().split())

dp = [[0]*(k+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(1, n+1):
    for j in range(k+1):
        for l in range(max(j-m, 0), j):
            dp[i][j] += dp[i-1][l]
            dp[i][j] %= mod
            
print(sum(dp[-1])%mod)
# for i in range(len(dp)): print(dp[i])