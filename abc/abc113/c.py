n, m = map(int, input().split())
py = [list(map(int, input().split())) for _ in range(m)]

py2 = py.copy()
py2.sort()

d = {}
t = 1
for i in range(m):
    p, y = py2[i][0], py2[i][1]
    if i==0: number=str(p).zfill(6)+str(1).zfill(6)
    else:
        if p==py2[i-1][0]:
            t += 1
            number = str(p).zfill(6)+str(t).zfill(6)
        else:
            t = 1
            number = str(p).zfill(6)+str(t).zfill(6)

    d[(p, y)] = number

for p, y in py:
    print(d[(p, y)])