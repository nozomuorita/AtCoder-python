n, t = map(int, input().split())
a = [int(input()) for _ in range(n)]

ans = 0
time = 0
for i in range(n):
    if a[i]>=time:
        ans += t
    else:
        ans += (a[i] + t - time)
    time = a[i] + t
    print(ans, time)

print(ans)