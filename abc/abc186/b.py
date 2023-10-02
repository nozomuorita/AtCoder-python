h, w = map(int, input().split())
a = []
for i in range(h):
    _ = list(map(int, input().split()))
    a.append(_)
    
mn = 101
for i in range(h):
    tmp = min(a[i])
    if tmp < mn:
        mn = tmp
        
ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j]>mn:
            ans += a[i][j] - mn
            
print(ans)