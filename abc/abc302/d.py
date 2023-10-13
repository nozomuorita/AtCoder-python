from bisect import bisect_left, bisect_right, insort_left, insort_right
n, m, d = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

ans = -1
for i in range(n):
    idx1 = min(bisect_left(b, a[i]+d), len(b)-1)
    idx2 = min(bisect_left(b, a[i]-d), len(b)-1)
    
    if abs(a[i]-b[idx1])<=d: ans=max(ans, a[i]+b[idx1])
    if abs(a[i]-b[idx2])<=d: ans=max(ans, a[i]+b[idx2])
        
print(ans)