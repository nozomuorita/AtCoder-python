from bisect import bisect_left, bisect_right, insort_left, insort_right
n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = bisect_right(a, x)
print(ans)