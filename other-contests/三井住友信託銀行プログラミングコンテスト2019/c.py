x = int(input())

dp = [0] * (x+1)
for i in range(100, 106):
    if i<=x: dp[i]=1

for i in range(x+1):
    if dp[i]:
        for j in range(100, 106):
            if i+j<=x: dp[i+j]=1

print(dp[x])