n = int(input())
t = list(map(int, input().split()))
s = sum(t)

# dp[i][j]: i番目までの料理を考え、合計時間をjとできるか(一つ目の電子レンジについて考える)
dp = [[False]*(s+1) for _ in range(n+1)]
dp[0][0] = True

for i in range(n):
    for j in range(s+1):
        if dp[i][j]:
            dp[i+1][j] = True           #  i番目の料理を一つ目の電子レンジで使わない場合
            dp[i+1][j+t[i]] = True      #  i番目の料理を一つ目の電子レンジで使う場合
            
ans = s
for i in range(s+1):
    if dp[-1][i]:                       #  n品目まで考えて、一つ目の電子レンジの時間をiとすることができるなら
        ans = min(ans, max(i, s-i))     #  一つ目の電子レンジは時間i、もう一つはs-iだけかかる
print(ans)