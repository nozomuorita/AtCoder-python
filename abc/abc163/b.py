n, m = map(int, input().split())
a = list(map(int, input().split()))

if (sum(a)<=n):
    ans = n - sum(a)
else:
    ans = -1
print(ans)