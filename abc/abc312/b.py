n, m = map(int, input().split())
s = [input() for _ in range(n)]
ans = []


b = []
for i in range(n-9+1):
    for j in range(m-9+1):
        if s[i][j] == '#':
            f = True
            for k in range(3):
                for l in range(3):
                    if s[i+k][j+l]=='.':
                        f = False
            if f:
                b.append([i, j])
            
for b_ in range(len(b)):
    x, y = b[b_][0], b[b_][1]

    # 右下黒の確認
    f = True
    for i in range(6, 9):
        for j in range(6, 9):
            if s[x+i][y+j] == '.':
                f = False
                break
    
    if not(f):
        continue

    # 周り白確認
    # 左上
    f = True
    for i in range(0, 4):
        if i != 3:
            if s[x+i][y+3]=='#':
                f = False
        else:
            if (s[x+i][y+0]=='#') or (s[x+i][y+1]=='#') or (s[x+i][y+2]=='#') or (s[x+i][y+3]=='#'):
                f = False

    if not(f):
        continue

    f = True
    for i in range(5, 9):
        if i != 5:
            if s[x+i][y+5]=='#':
                f = False
        else:
            if (s[x+i][y+5]=='#') or (s[x+i][y+6]=='#') or (s[x+i][y+7]=='#') or (s[x+i][y+8]=='#'):
                f = False

    if not(f):
        continue

    ans.append((x+1, y+1))

for i in ans:
    print(*i)


