"""
・二次元累積和
"""
h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(h)]

# black
black = [[0]*(w+1) for _ in range(h+1)]
for i in range(h):
    for j in range(w):
        if i%2==0:
            if j%2==0:
                black[i+1][j+1] = black[i+1][j] + c[i][j]
            else:
                black[i+1][j+1] = black[i+1][j]
        else:
            if j%2==1:
                black[i+1][j+1] = black[i+1][j] + c[i][j]
            else:
                black[i+1][j+1] = black[i+1][j]

for i in range(h-1):
    for j in range(w):
        black[i+2][j+1] += black[i+1][j+1]

# white
white = [[0]*(w+1) for _ in range(h+1)]
for i in range(h):
    for j in range(w):
        if i%2==1:
            if j%2==0:
                white[i+1][j+1] = white[i+1][j] + c[i][j]
            else:
                white[i+1][j+1] = white[i+1][j]
        else:
            if j%2==1:
                white[i+1][j+1] = white[i+1][j] + c[i][j]
            else:
                white[i+1][j+1] = white[i+1][j]

for i in range(h-1):
    for j in range(w):
        white[i+2][j+1] += white[i+1][j+1]

ans = 0
for i in range(h):
    for j in range(w):
        for k in range(i, h):
            for l in range(j, w):
                bl = black[k+1][l+1]
                wh = white[k+1][l+1]
                bl -= (black[k+1][j] + black[i][l+1])
                bl += black[i][j]
                wh -= (white[k+1][j] + white[i][l+1])
                wh += white[i][j]

                if bl==wh:
                    score = (k-i+1) * (l-j+1)
                    ans = max(ans, score)

print(ans)