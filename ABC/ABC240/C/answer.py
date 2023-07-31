# 解説AC
n, x = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

# dpテーブルを定義
# dp[i][j]: i回目のジャンプをして、jにたどり着くことができるか(できるなら１)
dp = [[0]*(x+1) for _ in range(n+1)]
dp[0][0] = 1 # 初期値

for i in range(n):
    for j in range(x):
        # i回目のジャンプでjにいることができるなら
        if dp[i][j]==1:
            # 飛んだあとにxを超えないなら
            if j+ab[i][0] <= x:
                dp[i+1][j+ab[i][0]] = 1
            if j+ab[i][1] <= x:
                dp[i+1][j+ab[i][1]] = 1

print('Yes' if dp[-1][-1]==1 else 'No')