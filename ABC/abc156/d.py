from math import factorial
def c(n, r):
    res = 1
    for i in range(1, r + 1):
        res *= (n - i + 1)
        res *= pow(i, mod - 2, mod)
        res %= mod
    return res

n, a, b = map(int, input().split())
mod = 10**9+7

ans = pow(2, n, mod)
ans -= 1

a_num = c(n, a)
b_num = c(n, b)
ans -= a_num
ans -= b_num
print(ans % mod)