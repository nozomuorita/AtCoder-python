from bisect import bisect_left, bisect_right, insort_left, insort_right
n, m = map(int, input().split())
x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
t = 0
f = True
while 1:
    if f:
        idx = bisect_left(a, t)
        if idx==n: break
        t = a[idx]+x
        f = not(f)
        ans += 1
    else:
        idx = bisect_left(b, t)
        if idx==m: break
        t = b[idx]+y
        f = not(f)
        ans += 1

print(ans//2)