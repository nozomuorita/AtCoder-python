n = int(input())
h = list(map(int, input().split()))

# dp[i]: 足場iに到達するために必要な最小コスト
dp = [0] * n

for i in range(n):
    if (i-1>=0) and (i-2>=0):
        dp[i] = min(dp[i-1]+abs(h[i]-h[i-1]), dp[i-2]+abs(h[i]-h[i-2]))
    elif (i-1>=0):
        dp[i] = dp[i-1] + abs(h[i]-h[i-1])
    else:
        continue

print(dp[-1])