"""
・表にした時と裏にした時の経路を記録しながらdp
・一つのパターンがわかればいいので、遷移先が空文字列でない(すでにその和になるパターンが見つかっているなら更新する必要ない)
"""
n, s = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j]: i枚目まで決めて、和をjとすることができるか
dp = [[""]*(s+1) for _ in range(n+1)]
dp[0][0] += "1"                        # 最初はダミーとして1を入れておく(if dp[i][j]に引っかかるように)

for i in range(n):
    for j in range(s):
        if dp[i][j]:
            if j+ab[i][0]<(s+1) and len(dp[i+1][j+ab[i][0]])==0: dp[i+1][j+ab[i][0]] = dp[i][j] + "H"  # 表の場合
            if j+ab[i][1]<(s+1) and len(dp[i+1][j+ab[i][1]])==0: dp[i+1][j+ab[i][1]] = dp[i][j] + "T"  # 裏の場合
           
if dp[-1][-1]:
    print('Yes')
    print(dp[-1][-1][1:])
else: print('No') 