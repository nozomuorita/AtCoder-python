n, x = map(int, input().split())
a = list(map(int, input().split()))

p = 0
for i in range(n):
    if i%2 == 0:
        p += a[i]
    else:
        p += a[i] - 1

if p <= x:
    print('Yes')
else:
    print('No')