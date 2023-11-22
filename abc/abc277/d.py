n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = sum(a)
for i in range(n): a.append(a[i]+m)

score = a[0]
mx = 0
for i in range(1, 2*n):
    if a[i]-a[i-1]<=1:
        score += a[i]%m
    else:
        score = a[i]%m
    mx = max(mx, score)

if mx>s: mx=s
print(s-mx)