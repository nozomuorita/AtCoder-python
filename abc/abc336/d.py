n = int(input())
a = list(map(int, input().split()))

left, l = [0]*n, 0
right, r = [0]*n, 0
for i in range(n):
    left[i] = min(a[i], l+1)
    l = left[i]
for i in range(n-1, -1, -1):
    right[i] = min(a[i], r+1)
    r = right[i]

ans = -float("inf")
for i in range(n):
    ans = max(ans, min(left[i], right[i]))
print(ans)