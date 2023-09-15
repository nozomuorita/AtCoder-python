import bisect

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
ans = 10**10

for i in range(n):
    idx = bisect.bisect_left(b, a[i])
    if idx == len(b):
        tmp = abs(a[i]-b[idx-1])
    elif idx == 0:
        tmp = abs(a[i]-b[idx])
    else:
        tmp = min(abs(a[i]-b[idx]), abs(a[i]-b[idx-1]))
    if tmp < ans:
        ans = tmp
        
print(ans)