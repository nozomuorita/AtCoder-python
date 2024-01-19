n, r = map(int, input().split())
mod = 10**9+7

bunbo = 1
for i in range(2, n+1):
    bunbo *= i
    bunbo %= mod

bunsi1 = 1
for i in range(2, r+1):
    bunsi1 *= i
    bunsi1 %= mod
bunsi2 = 1
for i in range(2, n-r+1):
    bunsi2 *= i
    bunsi2 %= mod

bunsi = bunsi1 * bunsi2
bunsi %= mod

ans = bunbo * pow(bunsi, mod-2, mod)
ans %= mod
print(ans)