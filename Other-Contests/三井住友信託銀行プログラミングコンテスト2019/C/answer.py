x = int(input())

#  dp[i]: 金額をiとすることができるか(できるなら１）
dp = [0] * 100001
dp[0] = 1  # 0円にすることは可能

# i円にすることが可能であるかを考える
for i in range(100, len(dp)):
    # j円の品物を買うことでi円とできるか判定
    for j in range(100, 105+1):
        # (i-j)円が0未満なら飛ばす
        if (i-j)<0:
            continue
        # (i-j)円とすることができるなら、j円の品物を買うことでi円とすることができる
        if dp[i-j]==1:
            dp[i] = 1
            
if dp[x]:
    print(1)
else:
    print(0)