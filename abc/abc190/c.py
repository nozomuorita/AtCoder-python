"""
・bit全探索
"""
n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

k = int(input())
cd = [list(map(int, input().split())) for _ in range(k)]

ans = 0

for i in range(2**k):
    ball = set()
    for j in range(k):
        if (i >> j) & 1:
            ball.add(cd[j][0])
        else:
            ball.add(cd[j][1])

    l = 0
    for p in range(m):
        if (ab[p][0] in ball) and (ab[p][1] in ball):
            l += 1

    ans = max(ans, l)

print(ans)