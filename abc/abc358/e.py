"""
未AC
"""
from math import comb
#from tqdm import tqdm
#from scipy.special import comb
#from itertools import combinations as comb
k = int(input())
c = list(map(int, input().split()))
mod = 998244353

# dp[i][j]: i番目の文字まで見て、総文字数がj個あるときの文字列数
dp = [[-1]*(k+1) for _ in range(27)]
dp[0][0] = 0

memo = {}

for i in range(26):
    for j in range(k+1):
        if dp[i][j]==-1: continue
        
        # その文字を使わない場合
        if dp[i+1][j]==-1:
            dp[i+1][j]=dp[i][j]
            dp[i+1][j] %= mod
        else:
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= mod
        # 文字を使う
        for l in range(1, c[i]+1):
            if j+l>k: break
            
            if dp[i+1][j+l]==-1:
                if dp[i][j]==0:
                    dp[i+1][j+l] = 1
                else:
                    if (j+1, l) in memo:
                        co = memo[(j+1, l)]
                    else:
                        co = pow(j+1, l, mod)
                        memo[(j+1, l)] = co
                    dp[i+1][j+l] = (dp[i][j] * (co%mod)) % mod
            else:
                if dp[i][j]==0:
                    dp[i+1][j+l] += 1
                else:
                    if (j+1, l) in memo:
                        co = memo[(j+1, l)]
                    else:
                        co = pow(j+1, l, mod)
                        memo[(j+1, l)] = co
                    dp[i+1][j+l] += (dp[i][j] * (co%mod)) % mod
            
            dp[i+1][j+l] %= mod

ans = 0
for i in dp[-1][1:]:
    if i!=-1:
        ans += i
        ans %= mod

print(ans%mod)
# for i in dp[:4]: print(i)
print(dp[-1])