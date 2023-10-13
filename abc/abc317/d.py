def ceil_div(x, y): return -(-x//y)
n = int(input())
inf = float('inf')
xyz = []
z_sum = 0                               #  議席総数
now = 0                                 #  今、持っている議席数
w = []                                  #  w[i]: i番目の選挙区をとるために鞍替えさせる必要のある人数
for i in range(n):
    x, y, z = map(int, input().split())
    xyz.append([x, y, z])
    z_sum += z
    if ceil_div(y-x, 2)>0: w.append(ceil_div(y-x, 2))   #  選挙区をとるためには、ceil((y-x)/2)人必要
    else:
        w.append(0)                                     #  すでに高橋派が多数派なら0人
        now += z

need = ceil_div(z_sum, 2) - now                         #  必要議席数
if need<=0:                                             #  すでに過半数の議席を持っているなら0
    print(0)
    exit()

# dp[i][j]: i番目の選挙区までを考えて、高橋派の議席をjとするときに必要な最小コスト(鞍替人数)
dp = [[inf]*(z_sum+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1, n+1):
    for j in range(z_sum+1):
        # i番目の議席をとらない場合 -> i-1番目と同じ
        dp[i][j] = min(dp[i][j], dp[i-1][j])
        # i番目の議席をとる -> i番目の議席をとるために必要な鞍替人数を加算
        if j-xyz[i-1][2]>=0:
            dp[i][j] = min(dp[i][j], dp[i-1][j-xyz[i-1][2]]+w[i-1])
        
ans = inf
for i in range(ceil_div(z_sum, 2), z_sum+1):
    ans = min(ans, dp[-1][i])
print(ans)