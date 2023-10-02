"""
・動的計画法
・1段前まで行く方法とl段前まで行く通りを足して遷移
"""

mod = 10**9+7
n, l = map(int, input().split())
dp = [0]*(n+1)
dp[0] = 1

for i in range(1, n+1):
    dp[i] = dp[i-1]
    if i-l>=0:
        dp[i] += dp[i-l]
    dp[i] %= mod

print(dp[-1])