n, k, d = map(int, input().split())
a = list(map(int, input().split()))

# dp[i][j][l]: i番目の項まで考えて、j個選んだ時のmodDがlである和の最大値
dp = []
for i in range(n+1):
    t = []
    for j in range(k+1):
        t.append([-1]*d)
    dp.append(t)
dp[0][0][0] = 0      # 初期値: 0番目の項まで考えて、0個選んだときのmodDが0である和の最大値は0

for i in range(n):
    for j in range(k+1):
        for l in range(d):
            if dp[i][j][l]==-1: continue
            dp[i+1][j][l] = max(dp[i][j][l], dp[i+1][j][l])            #  a[i]を選ばない場合
            if j==k: continue                                          #  j==k(k個選んでいる)場合はさらに選ぶことができないので選んだ場合は考えない
            t = (dp[i][j][l]+a[i]) % d                                 #  a[i]を選んだ場合のmodを計算
            dp[i+1][j+1][t] = max(dp[i+1][j+1][t], dp[i][j][l]+a[i])   #  計算したmodの位置にmaxで比較して入れる
            
print(dp[-1][-1][0])