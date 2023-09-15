n = int(input())
t = list(map(int, input().split()))
s = sum(t)

# dp[i][j]: i番目までの料理を考え、合計時間をjとできるか
dp = [[False]*(s+1) for _ in range(n+1)]
dp[0][0] = True

for i in range(n):
    for j in range(s+1):
        if dp[i][j]:
            dp[i+1][j] = True
            dp[i+1][j+t[i]] = True
            
ans = s
for i in range(s+1):
    if dp[-1][i]:
        ans = min(ans, max(i, s-i))
print(ans)