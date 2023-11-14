n = int(input())
a = list(map(int, input().split()))

ans = 0
l, r = 0, 0

for i in range(n):
    if r<l: r=l
    while r<(n-1) and a[r]<a[r+1]: r+=1
    ans += r-l+1
    l += 1
    
print(ans)