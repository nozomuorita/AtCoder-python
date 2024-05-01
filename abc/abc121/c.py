n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort()

ans = 0
cnt = 0
for i in range(n):
    a, b = map(int, ab[i])
    ans += a * (min(m-cnt, b))
    cnt += min(m-cnt, b)

print(ans)