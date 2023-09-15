n, w = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

ab.sort(reverse=True)
ans = 0

for a, b in ab:
    if b <= w:
        ans += a * b
        w -= b
    else:
        ans += a * w
        w -= w

    if w == 0:
        break

print(ans)