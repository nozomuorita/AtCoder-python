h, w = map(int, input().split())
a = [input() for _ in range(h)]

#  空白行、列
row, col = set(), set()
for i in range(h):
    if '#' not in a[i]: row.add(i)
for i in range(w):
    c = [r[i] for r in a]
    if '#' not in c: col.add(i)
    
for i in range(h):
    if i in row: continue
    ans = ''
    for j in range(w):
        if j in col: continue
        ans += a[i][j]
    
    print(ans)