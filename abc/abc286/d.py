n, x = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort()

# dp[i][j]: i個目の硬貨までを使って、j円払うことができるか
dp = [[False]*(x+1) for _ in range(n+1)]
dp[0][0] = True

for i in range(n):
    a, b = ab[i][0], ab[i][1]
    for j in range(x+1):
        if dp[i][j]==False: continue      #  i個目の硬貨まで使ってj円払うことができないならcontinue
        
        for k in range(b+1):              #  i個目の硬貨を0枚使う場合、1枚使う場合...としてTrueにしていく
            if j+a*k>x: break             #  x円を超えたら、break
            dp[i+1][j+a*k] = True
            
print('Yes') if dp[-1][-1] else print('No')