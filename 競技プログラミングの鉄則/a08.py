h, w = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(h)]

x_cum = [[0]*(w+1) for _ in range(h+1)]
for i in range(h):
    for j in range(w):
        if w==0: x_cum[i+1][j+1]=x[i][j]
        else: x_cum[i+1][j+1] = x_cum[i+1][j] + x[i][j]

for i in range(1, h):
    for j in range(w):
        x_cum[i+1][j+1] += x_cum[i][j+1]

q = int(input())
for _ in range(q):
    a, b, c, d = list(map(int, input().split()))
    ans = x_cum[c][d] + x_cum[a-1][b-1] - x_cum[a-1][d] - x_cum[c][b-1]
    print(ans)