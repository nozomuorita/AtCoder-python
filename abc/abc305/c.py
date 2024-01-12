h, w = map(int, input().split())
s = [input() for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j]=="#": continue
        sharpe = 0
        for d1, d2 in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=(i+d1)<h and 0<=(j+d2)<w and s[i+d1][j+d2]=="#": sharpe+=1
        
        if sharpe>1: exit(print(i+1, j+1))