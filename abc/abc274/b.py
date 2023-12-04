h, w = map(int, input().split())
c = [input() for _ in range(h)]

ans = []
for i in range(w):
    t = 0
    for j in range(h):
        if c[j][i]=="#": t+=1
    ans.append(t)

print(*ans)