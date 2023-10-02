"""
・動的計画法
・dp[i]: 総和がiとなる数列の個数として遷移
・dp[0]=1(初期値)
"""

s = int(input())
mod = 10**9+7

dp = [0]*(s+1)
dp[0] = 1

for i in range(3, s+1):
    t = 0
    idx = 3
    while i-idx>=0:
        t += dp[i-idx]
        t %= mod
        idx += 1
    dp[i] = t % mod

print(dp[-1]%mod)