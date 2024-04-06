h, w, n = map(int, input().split())
t = input()
s = [input() for _ in range(h)]
ans = 0

visited = [[False]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j]=="#": continue
        ok = True
        x = i
        y = j
        for k in range(n):
            if t[k]=="L": d1, d2 = 0, -1
            elif t[k]=="R": d1, d2 = 0, 1
            elif t[k]=="U": d1, d2 = -1, 0
            elif t[k]=="D": d1, d2 = 1, 0
            
            x+=d1; y+=d2
            if 0<=x<h and 0<=y<w and s[x][y]!="#": continue
            else:
                ok = False
                break

        if ok and visited[x][y]==False: 
            ans+=1
            visited[x][y] = True

print(ans)