H, W = map(int, input().split())
S = []
for i in range(H):
    s = input()
    S.append(s)
    
snuke = 'snuke'
    
# まずは，sを探す
for i in range(H):
    for j in range(W):
        s = S[i][j]
        if s == 's':
            for i2, j2, m in [[i+1, j, 1], [i-1, j, 2], [i, j+1, 3], [i, j-1, 4], [i-1, j-1, 5], [i-1, j+1, 6], [i+1, j+1, 7], [i+1, j-1, 8]]:
                ans = [(i+1, j+1)]
                for _ in range(4):
                    if (i2<0) or (i2 >H-1) or (j2<0) or (j2>W-1):
                        break
                    if S[i2][j2] == snuke[_+1]:
                        ans.append((i2+1, j2+1))
                        if m==1:
                            i2 += 1
                        elif m==2:
                            i2 -= 1
                        elif m==3:
                            j2 += 1
                        elif m==4:
                            j2 -= 1
                        elif m==5:
                            i2 -= 1
                            j2 -= 1
                        elif m==6:
                            i2 -= 1
                            j2 += 1
                        elif m==7:
                            i2 += 1
                            j2 += 1
                        elif m==8:
                            i2 += 1
                            j2 -= 1
                        
                    if len(ans) == 5:
                        for o in ans:
                            print(*o)
                        exit()