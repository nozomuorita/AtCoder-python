"""しゃくとり法"""
n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
idx = 0
for i in range(n):
    while idx+1<n and a[idx+1]-a[i]<=k:
        idx += 1
    
    ans += idx-i

print(ans)