# bit全探索
n, m, x = map(int, input().split())
c, a = [], []
for i in range(n):
    list_ = list(map(int, input().split()))
    c.append(list_[0])
    a.append(list_[1:])
    
ans = 10**10
for i in range(2**n):
    tmp = [0] * m
    t = 0
    for j in range(n):
        if (i>>j) & 1:
            t += c[j]
            for k in range(m):
                tmp[k] += a[j][k]
    #print(i, t, tmp)
    if min(tmp)>=x:
        if t<ans:
            ans = t

if ans == 10**10:
    print(-1)
else:
    print(ans)