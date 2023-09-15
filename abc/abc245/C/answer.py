n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# dp配列を定義
# dp[i][j]: j(A_i or B_i)を用いて長さ i の配列を作ることができるかどうか(できるなら１)
dp = [[0, 0] for _ in range(n)]
dp[0][0], dp[0][1] = 1, 1 # 初期値(a_0を用いて、長さ1の数列を作ることは可能なので１とする。bも同様)

# a[1:], b[1:]を見ていく(長さ２以上の場合を埋めていく)
for i in range(1, n):
    # a_iを使うとき
    # dp[i-1][0]が１(a[i-1]を用いて長さi-1の数列を作ることができる)かつ、a[i]を用いたときのabsがk以下なら１
    if (dp[i-1][0]==1) and (abs(a[i-1] - a[i])<=k):
        dp[i][0] = 1
    if (dp[i-1][1]==1) and (abs(b[i-1] - a[i])<=k):
        dp[i][0] = 1

    # B_iを使うとき
    if (dp[i-1][0]==1) and (abs(a[i-1] - b[i])<=k):
        dp[i][1] = 1
    if (dp[i-1][1]==1) and (abs(b[i-1] - b[i])<=k):
        dp[i][1] = 1

# どちらかが１ならok
if (dp[-1][0]==1) or (dp[-1][1]==1):
    print('Yes')
else:
    print('No')