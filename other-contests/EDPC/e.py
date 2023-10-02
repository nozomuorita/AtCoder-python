n, w = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]

sum_v = 0
for i in range(n):
    sum_v += wv[i][1]
# dp[i][j]: 品物iまで考えて、価値の合計をjとしたときの最小重さ
dp = [[10**10]*(sum_v+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1, n+1):
    for j in range(sum_v+1):
        if (j-wv[i-1][1])<0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-wv[i-1][1]]+wv[i-1][0])

for i in range(sum_v, -1, -1):
    if dp[-1][i]<=w:
        ans = i
        break
print(ans)