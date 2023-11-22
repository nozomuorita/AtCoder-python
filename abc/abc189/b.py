n, x = map(int, input().split())
vp = [list(map(int, input().split())) for _ in range(n)]

alcohol = 0
for i in range(n):
    alcohol += (vp[i][0]) * (vp[i][1])
    if alcohol>x*100:
        print(i+1)
        exit()
print(-1)