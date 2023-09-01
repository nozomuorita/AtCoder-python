# 逐次modをとる→とらないとTLE
n = int(input())
mod = 998244353

# dp[i][j]: i桁目まで考えて、i桁目をjとするパターン数
dp = [[0]*9 for _ in range(n)]
# 0桁目(最初)はすべてについて1とおり
for i in range(9):
    dp[0][i] = 1

for i in range(1, n):
    dp[i][0] = (dp[i-1][1] + dp[i-1][0]) % mod
    
    for j in range(1, 8):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1] + dp[i-1][j]) % mod
        
    dp[i][8] = (dp[i-1][7] + dp[i-1][8]) % mod
    
ans = sum(dp[-1]) % mod
print(ans)