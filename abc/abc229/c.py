n, w = map(int, input().split())
ab = sorted([list(map(int, input().split())) for _ in range(n)], reverse=True)

ans = 0
weight = 0
for i in range(n):
    a, b = map(int, ab[i])
    if weight+b<=w:
        ans += (a*b)
        weight += b
    else:
        while weight<w:
            weight += 1
            ans += a
        break

print(ans)