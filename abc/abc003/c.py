n, k = map(int, input().split())
r = list(map(int, input().split()))
r.sort(reverse=True)

ans = 0
for i in range(k-1, -1, -1):
    ans = (ans+r[i])/2
    
print(ans)