h, w, n = map(int, input().split())
c = [["."]*w for _ in range(h)]

# 0: 上, 1: 右, 2: 下, 3: 左
i, j, d = 0, 0, 0
for _ in range(n):
    if c[i][j]==".":
        c[i][j] = "#"
        d += 1
        d %= 4
    else:
        c[i][j] = "."
        if d==0: d=3
        else: d-=1
    
    if d==0:
        if i==0: i=h-1
        else: i-=1
    elif d==1:
        if j==w-1: j=0
        else: j+=1
    elif d==2:
        if i==h-1: i=0
        else: i+=1
    else:
        if j==0: j=w-1
        else: j-=1

for i in range(h):
    print("".join(c[i]))