n = int(input())
a = list(map(int, input().split()))
a_sum = sum(a)

ans = 0
for i in range(n):
    ans += (a[i]**2) * (n-1)
    ans -= a[i] * (a_sum - a[i])

print(ans)