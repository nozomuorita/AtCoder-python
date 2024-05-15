from bisect import bisect_left, bisect_right, insort_left, insort_right
n = int(input())
a = sorted(list(map(int, input().split())))

ans = 0

for i in range(n):
    mid = a[i]
    left = bisect_left(a, mid)
    right = bisect_right(a, mid)
    
    ans += left*(n-right)

print(ans)