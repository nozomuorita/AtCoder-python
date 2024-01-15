n, s = map(int, input().split())
a = list(map(int, input().split()))

# dp[i][j]: i枚目までの中から選んで、合計をjとすることができるか
dp = [[False]*(s+1) for i in range(n+1)]
dp[0][0] = True

for i in range(n):
    for j in range(s+1):
        if dp[i][j]:
            dp[i+1][j] = True
            if j+a[i]<=s:
                dp[i+1][j+a[i]] = True

print('Yes') if dp[-1][-1] else print('No')