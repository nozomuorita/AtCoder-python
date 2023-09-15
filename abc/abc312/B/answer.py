n, m = map(int, input().split())
s = [input() for _ in range(n)]
ans = []

# 左上に該当するマスを探す
b = []
for i in range(n-9+1): # (n-1-8)までが対象
    for j in range(m-9+1): # (m-1-8)までが対象
        # もし'#'なら周りの9マスを見て、すべて黒か確認
        if s[i][j] == '#':
            f = True
            for k in range(3):
                for l in range(3):
                    if s[i+k][j+l]=='.':
                        f = False
            # すべて黒ならば、bに追加
            if f:
                b.append([i, j])
            
# 各マスについて、残りの条件を判定
for b_ in range(len(b)):
    x, y = b[b_][0], b[b_][1]

    # 右下黒の確認
    f = True
    for i in range(6, 9):
        for j in range(6, 9):
            if s[x+i][y+j] == '.':
                f = False
                break
    # 右下9マスが黒でないならば、continue
    if not(f):
        continue

    # 周りの白確認
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

    # 右下
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

    # すべて満たすなら、ansに追加
    ans.append((x+1, y+1))

for i in ans:
    print(*i)