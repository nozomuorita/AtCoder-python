mod = 998244353
n, x = map(int, input().split())
t = list(map(int, input().split()))
    
# dp[i]: 時刻iで曲が終わる確率
dp = [0]*(x+1)
dp[0] = 1

pow_n = pow(n, -1, mod)

for i in range(x):
    for j in t:
        if i+j<=x:
            dp[i+j] += dp[i]*pow_n
            dp[i+j] %= mod
            
ans = 0
if x-t[0]+1<=0:
    start = 0
else:
    start = x-t[0]+1
for i in range(start, x+1):
    ans += dp[i]
    
print(ans*pow_n%mod)