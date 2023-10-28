n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[0, 0] for _ in range(n)]
dp[0][0] = 1
dp[0][1] = 1

for i in range(1, n):
    if dp[i-1][0]==1:
        num1 = abs(a[i]-a[i-1])
        num2 = abs(b[i]-a[i-1])
        if num1 <= k:
            dp[i][0] = 1
        if num2 <= k:
            dp[i][1] = 1
    if dp[i-1][1]== 1:
        num3 = abs(a[i]-b[i-1])
        num4 = abs(b[i]-b[i-1])

        if num3 <= k:
            dp[i][0] = 1
        if num4 <= k:
            dp[i][1] = 1

if (dp[-1][0]==1) or (dp[-1][1]==1):
    print('Yes')
else:
    print('No')