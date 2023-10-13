"""
・dp
・dp[i][j]: i番目の項まで考えて、j項選んだ時の最大値(iは0-index)
・初期値: dp[0][0]=0(=0番目の項まで考えて、0個選んだときの和=0)
・初期値2: dp[0][1]=a[0](=0番目の項まで考えて、1個選んだときの最大値=a[0])
・dpテーブルの更新↓
・i番目の項を選ばない場合(=(i-1)番目まで考えてj個選んだ場合=dp[i-1][j])と選んだ場合(=(i-1)番目の項まで考えてj-1個選んだときの最大値+i番目の項*i=dp[i-1][j-1]+(a[i]*j))
"""

n, m = map(int, input().split())
a = list(map(int, input().split()))

# dp[i][j]: i番目の項まで考えて、j個選んだ時の最大値(i: 0-index)
dp = [[-10**18]*(n+1) for _ in range(n)]
dp[0][0] = 0
dp[0][1] = a[0]

for i in range(1, n):
    for j in range(i+2):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+(a[i]*j))
        
print(dp[-1][m])