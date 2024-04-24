h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

row_cum = []
for i in range(h):
    row_cum.append(sum(a[i]))
col_cum = []
for i in range(w):
    s = 0
    for j in range(h):
        s += a[j][i]
    col_cum.append(s)

ans = []
for i in range(h):
    l = []
    for j in range(w):
        score = row_cum[i] + col_cum[j] - a[i][j]
        l.append(score)
    ans.append(l)

for i in ans:
    print(*i)