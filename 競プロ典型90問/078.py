import bisect
n, m = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

ans = 0
for i in range(n):
    tmp = g[i]
    tmp.sort()
    # 二分探索で挿入点を探す
    num = bisect.bisect_right(tmp, i)
    if num == 1:
        ans += 1

print(ans)