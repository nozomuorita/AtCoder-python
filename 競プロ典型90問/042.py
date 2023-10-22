k = int(input())
mod = 10**9+7

if k%9!=0: exit(print(0))

# dp[i]: 各桁の和がiとなる通り数
dp = [0]*(k+1)
dp[0] = 1

for i in range(1, k+1):
    for j in range(1, 10):
        if i-j<0: break
        dp[i] += dp[i-j]
        dp[i] %= mod
        
print(dp[-1])