"""LCS"""
s = input()
t = input()

# dp[i][j]: Sのi文字目、Tのj文字目まで見たときのLCS
dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]

for i in range(len(s)):
    for j in range(len(t)):
        if s[i]==t[j]:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
        else:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1], dp[i+1][j])
        
ans = dp[-1][-1]
print(ans)