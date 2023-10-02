mod = 998244353
s = input()

dp = [[0]*(len(s)+1) for _ in range(len(s)+1)]
dp[0][0] = 1

for i in range(len(s)):
    if s[i]=='(':
        for j in range(1, len(s)+1):         
            dp[i+1][j] = dp[i][j-1]
    elif s[i]==')':
        for j in range(len(s)):
            dp[i+1][j] = dp[i][j+1]
    else:
        dp[i+1][0] = dp[i][1]
        dp[i+1][-1] = dp[i][-2]
        for j in range(1, len(s)):
            dp[i+1][j] = (dp[i][j-1]+dp[i][j+1]) % mod
            
print(dp[-1][0] % mod)