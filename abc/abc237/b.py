h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

b = []
for i in range(w):
    tmp = [0]*h
    b.append(tmp)

for i in range(h):
    for j in range(w):
        b[j][i] = a[i][j]
        
for i in range(w):
    print(*b[i])