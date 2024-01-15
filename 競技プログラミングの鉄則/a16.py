n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# dp[i]: i番目の部屋に行くのにかかる時間
dp = [10**18] * n
dp[0] = 0

for i in range(1, n):
    if i==1:
        dp[i] = min(dp[i], dp[i-1]+a[i-1])
    else:
        dp[i] = min(dp[i], dp[i-1]+a[i-1], dp[i-2]+b[i-2])

print(dp[-1])