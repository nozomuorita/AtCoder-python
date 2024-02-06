n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = -1
for i in range(2**n):
    x, y = 0, 0
    for j in range(n):
        if i>>j & 1:
            x += v[j]
            y += c[j]
    ans = max(ans, x-y)
print(ans)
