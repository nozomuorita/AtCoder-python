mod = 10**9+7
n, m = map(int, input().split())
if abs(n-m)>1: exit(print(0))

ans = 1
for i in range(1, max(n, m)+1):
    ans *= i
    ans %= mod
for i in range(1, min(n, m)+1):
    ans *= i
    ans %= mod

if n==m:
    ans *= 2
    ans %= mod
    
print(ans)