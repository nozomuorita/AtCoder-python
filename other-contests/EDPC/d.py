"""
・dp[i][j]: i番目の品物までを見て重さ合計をjとしたときの最大価値
・1<=n<=100で1<=w<=10**5なので、2重ループとしてもO(10**7)なので間に合う
"""

n, w = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j]: 品物iまで入れて、重さがj以下の時の最大価値
dp = [[0]*(w+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(w+1):
        #  もし、品物iを入れることができない(jから品物iの重さを引いたときに0以下になるなら入れることができない)場合は、品物を入れない
        if (j-wv[i-1][0])<0:
            dp[i][j] = dp[i-1][j]
        #  入れることができるなら、品物iを入れない場合と入れた場合で価値が大きいほうを採用
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-wv[i-1][0]]+wv[i-1][1])
        
print(dp[-1][-1])