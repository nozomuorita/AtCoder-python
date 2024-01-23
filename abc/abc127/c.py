n, m = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(m)]

l0 = lr[0][0]
r0 = lr[0][1]

for i in range(1, m):
    l = lr[i][0]
    r = lr[i][1]

    if l > l0:
        l0 = l
    if r < r0:
        r0 = r

if l0 > r0:
    ans = 0
else:
    ans = r0 - l0 +1

print(ans)