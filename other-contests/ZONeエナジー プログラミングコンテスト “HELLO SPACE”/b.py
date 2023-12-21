n, d, h = map(int, input().split())
dh = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    height = h - ((h-dh[i][1])/(d-dh[i][0]))*d
    ans = max(ans, height)

print(ans)