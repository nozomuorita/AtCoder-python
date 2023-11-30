n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
mod = 998244353

# dp[i][j]: i枚目まで決めて、i枚目がj(0: 表, 1: 裏)であるときの数
dp = [[0, 0] for _ in range(n)]
dp[0] = [1, 1]

for i in range(1, n):
    if ab[i][0]!=ab[i-1][0]: dp[i][0]+=dp[i-1][0]; dp[i][0]%=mod
    if ab[i][0]!=ab[i-1][1]: dp[i][0]+=dp[i-1][1]; dp[i][0]%=mod
    if ab[i][1]!=ab[i-1][0]: dp[i][1]+=dp[i-1][0]; dp[i][1]%=mod
    if ab[i][1]!=ab[i-1][1]: dp[i][1]+=dp[i-1][1]; dp[i][1]%=mod
    
print(sum(dp[-1])%mod)