n = int(input())
r = [int(input()) for _ in range(n)]
r.sort(reverse=True)

ans = 0
f = True
for i in range(n):
    if f:
        ans += r[i]**2
    else:
        ans -= r[i]**2
    f = not(f)

print(ans*(3.1415926535))