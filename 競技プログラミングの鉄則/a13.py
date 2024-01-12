from bisect import bisect_left, bisect_right, insort_left, insort_right
n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    idx = bisect_right(a, a[i]+k)
    ans += (idx - (i+1))

print(ans)