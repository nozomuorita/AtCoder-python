n = int(input())
a = list(map(int, input().split()))

cur = 1
for i in range(n):
    if a[i]==cur:
        cur += 1

ans = n - (cur - 1)
print(-1) if ans==n else print(ans)