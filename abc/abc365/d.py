n = int(input())
s = input()

dp = [[-1]*3 for _ in range(n+1)]
dp[0] = [0]*3

for i in range(n):
    for j in range(3):
        if dp[i][j]==-1: continue
        if s[i]=="R":
            if j==0 or j==1:
                dp[i+1][2] = max(dp[i+1][2], dp[i][j]+1)
            if j==0 or j==2:
                dp[i+1][1] = -1
            if j==1 or j==2:
                dp[i+1][0] = max(dp[i+1][0], dp[i][j])
        elif s[i]=="S":
            if j==0 or j==1:
                dp[i+1][2] = -1
            if j==0 or j==2:
                dp[i+1][1] = max(dp[i+1][1], dp[i][j])
            if j==1 or j==2:
                dp[i+1][0] = max(dp[i+1][0], dp[i][j]+1)
        else:
            if j==0 or j==1:
                dp[i+1][2] = max(dp[i+1][2], dp[i][j])
            if j==0 or j==2:
                dp[i+1][1] = max(dp[i+1][1], dp[i][j]+1)
            if j==1 or j==2:
                dp[i+1][0] = -1

print(max(dp[-1]))