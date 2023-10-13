"""
・dp
・dp[i][j]: i回目の操作を行ったときに挿入される値がjである通り
・初期値: dp[0][a[0]]=1(=0回目まで操作を行って左端にある値はa[0]なので、dp[0][a[0]]=1とする)
・dpテーブルをfor文で回していき、0でないなら2つの操作を行う
・ex)サンプル１
・dp[0][2]=1(初期値)であるので、x=2, y=a[0+1]=7として2つの挿入される値を計算(n1, n2とする)
・するとdp[1][n1]=dp[1][n2]=dp[0][2]となる
・これを繰り返す
"""

mod = 998244353
n = int(input())
a = list(map(int, input().split()))

# dp[i][j]: i回目の操作を行ったときに一番左端(挿入される値)がjである通り
dp = [[0]*10 for _ in range(n)]
dp[0][a[0]] = 1

for i in range(n-1):
    for j in range(10):
        if dp[i][j]==0: continue
        t1 = (j+a[i+1]) % 10
        t2 = (j*a[i+1]) % 10
        dp[i+1][t1] += dp[i][j] % mod
        dp[i+1][t2] += dp[i][j] % mod
        
for i in range(0, 10): print(dp[-1][i]%mod)