n, k = map(int, input().split())
a = list(map(int, input().split()))

s = 0
for i in range(k): s+=a[i]
ans = s

l = 0
r = k
while r<n:
    s -= a[l]
    s += a[r]
    ans += s
    l += 1
    r += 1
    
print(ans)