def ceil_div(x, y): return -(-x//y)
n, m = map(int, input().split())

ans = float('inf')
for i in range(1, int(ceil_div(m**0.5, 1)+1)):
    a = i
    b = ceil_div(m, a)
    if (1<=a<=n) and (1<=b<=n):
        ans = min(ans, a*b)

if ans==float('inf'): print(-1)
else: print(ans)