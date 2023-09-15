n = int(input())
a = list(map(int, input().split()))
a.sort()

for i in range(1, n):
    if (abs(a[i]-a[i-1])!=1):
        ans = a[i]-1
        break

print(ans)