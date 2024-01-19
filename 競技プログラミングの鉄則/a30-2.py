from math import factorial
n, r = map(int, input().split())
mod = 10**9+7

bunbo = factorial(n) % mod
bunsi = ((factorial(r)%mod) * (factorial(n-r)%mod) % mod)

ans = (bunbo * pow(bunsi, mod-2, mod)) % mod
print(ans)