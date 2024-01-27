n, m = map(int, input().split())
d = [[] for _ in range(n)]
for i in range(m):
    x, y = map(lambda x:x-1, map(int, input().split()))
    d[x].append(y)
    d[y].append(x)

ans = 1
for i in range(2**n):
    t = set()
    cnt = 0
    for j in range(n):
        if i>>j & 1:
            t.add(j)
            cnt += 1

    ok = True
    for j in t:
        if (set(d[j]+[j]) & t)==t: continue
        else:
            ok = False
            break

    if ok: ans=max(ans, cnt)

print(ans)