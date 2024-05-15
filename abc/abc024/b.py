n, t = map(int, input().split())
ans = 0
now = 0

for i in range(n):
    a = int(input())
    if a>now:
        ans += t
    else:
        ans += (a+t) - now
    now = a + t

print(ans)