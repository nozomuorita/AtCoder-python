"""ナップサックDP(重さ基準)"""
n, W = map(int, input().split())
weight, value = [], []
for i in range(n):
    _w, _v = map(int, input().split())
    weight.append(_w)
    value.append(_v)

# dp[i][j]: i番目の品物まで考えて、重さの合計をjとしたときの最大価値
dp = [[-1]*(W+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(n):
    for j in range(W+1):
        if dp[i][j]==-1: continue
        
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if j+weight[i]<=W:
            dp[i+1][j+weight[i]] = max(dp[i+1][j+weight[i]], dp[i][j]+value[i])

ans = max(dp[-1])
print(ans)