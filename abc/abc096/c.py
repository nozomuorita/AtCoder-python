h, w = map(int, input().split())
s = [input() for _ in range(h)]

for i in range(h):
    for j in range(w):
        t = s[i][j]
        if t != '#':
            continue
        f = False
        for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
            if (0<=i2<h) and (0<=j2<w):
                if s[i2][j2]=='#':
                    f = True
                    break
        if not f:
            print('No')
            exit()
            
print('Yes')