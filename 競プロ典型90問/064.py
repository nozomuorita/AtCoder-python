n, q = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
b = []
for i in range(n-1):
    b.append(a[i+1]-a[i])
    ans += abs(b[i])
b.append(0)

for i in range(q):
    l, r, v = map(int, input().split())
    l -= 1
    r -= 1
    before = abs(b[l-1])+abs(b[r])
    if l>=1:
        b[l-1] += v
    if r<(n-1):
        b[r] -= v
    after = abs(b[l-1])+abs(b[r])
    
    ans -= before
    ans += after
    print(ans)