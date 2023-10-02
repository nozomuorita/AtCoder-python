mod = 10**9+7

n, k = map(int, input().split())
ans = 0

for i in range(k, n+2):
    # print(i)
    mn = (i*(i-1)) // 2
    mx = (i*(2*n-i+1)) // 2
    # print(mn, mx)
    s = mx - mn + 1
    ans += s
    ans %= mod

print (ans%mod)