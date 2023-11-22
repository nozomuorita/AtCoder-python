n = int(input())
s = [input() for _ in range(n)]

# dp[i][j]: i番目の計算まで行って、yがj(0: False, 1: True)であるものの個数
dp = [[0, 0] for _ in range(n+1)]
dp[0][0], dp[0][1] = 1, 1                        #  最初(計算前)はTrueとFalseそれぞれ1通り

for i in range(n):
    if s[i]=="AND":
        dp[i+1][0] = (dp[i][0]*2) + dp[i][1]     #  i番目までの計算でFalseの場合は、i番目がTrueでもFalseでもFalseとなるので2倍
        dp[i+1][1] = dp[i][1]                    #  i番目までの計算でTrueでなければ、ANDをとってTrueとすることはできない
    else:
        dp[i+1][0] = dp[i][0]                    #  i番目まで計算してTrueの場合、TrueとしてもFalseとしてもTrueとなってしまうのでdp[i][1]は足さない
        dp[i+1][1] = dp[i][0] + (dp[i][1]*2)     #  i番目までの計算でTrueなら、TとFどちらをとっても良いので2倍
        
print(dp[-1][1])