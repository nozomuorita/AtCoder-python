from bisect import bisect_left, bisect_right, insort_left, insort_right

n, m, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
ans = 0

bcum = [0]
for i in range(m):
    bcum.append(bcum[i]+b[i])
    
for i in range(n):
    
    idx = bisect_left(b, p-a[i])
    # print(idx)
    ans += (idx*a[i]) + bcum[idx]
    ans += (len(b)-idx) * p
        
print(ans)