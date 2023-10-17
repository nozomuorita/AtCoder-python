h, w = map(int, input().split())
c = [input() for _ in range(h)]

ans = [0]*(min(h, w)+1)  # ans[i]: サイズiのバツ印

for i in range(h):
    for j in range(w):
        if c[i][j]=='.': continue
        n = 1
        while 1:
            t1, t2 = 0, 0  # t1: '#', t2: '.'
            for i2, j2 in [[n, n], [n, -n], [-n, -n], [-n, n]]:
                if not((0<=i+i2<h) and (0<=j+j2<w)):
                    t2+=1
                    continue
                if c[i+i2][j+j2]==".": t2+=1
                else: t1+=1
            if t1==4: n+=1
            else:
                ans[n-1]+=1
                break

print(*ans[1:])