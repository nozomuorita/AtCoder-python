from bisect import bisect_left, bisect_right, insort_left, insort_right
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

ans = -1
for i in range(n):
    s = a[i] + m
    idx = bisect_left(a, s)
    x = idx - i
    ans = max(ans, x)
    
print(ans)