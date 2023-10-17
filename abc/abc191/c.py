h, w = map(int, input().split())
c = [input() for _ in range(h)]

ans = 0
for i in range(h-1):
    for j in range(w-1):
        # if c[i][j]=='.': continue
        cnt = 0
        for i2, j2 in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            if c[i+i2][j+j2]=='.': cnt+=1
        
        if cnt==1 or cnt==3: ans+=1
        
print(ans)