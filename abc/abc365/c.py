from bisect import bisect_left, bisect_right, insort_left, insort_right
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
a_sum = sum(a)
a_cum = [0]
for i in range(n):
    a_cum.append(a_cum[-1]+a[i])

if a_sum<=m:
    exit(print("infinite"))

left = 0
right = 10**18

while right-left>1:
    mid = (left+right)//2
    idx = bisect_right(a, mid)
    
    if idx==n:
        score = a_sum
    else:
        score = a_cum[idx] + (mid * (n-idx))
    
    if score>m:
        right = mid
    else:
        left = mid

print(left)