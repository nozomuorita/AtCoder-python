H, W, n, h, w = map(int, input().split())
a = [list(map(int, input().split())) for i in range(H)]

ans = [[0]*(W-w+1) for _ in range(H-h+1)]

cnt = []
for i in range(H):
    tmp = []
    for j in range(W):
        tmp2 = [0]*(n+1)
        tmp2[a[i][j]] += 1
        tmp.append(tmp2)
    cnt.append(tmp)

for i in range(H):
    cnt[i].append([0]*(n+1))
tmp = []
for i in range(W+1): tmp.append([0]*(n+1))
cnt.append(tmp)
    
for i in range(H):
    for j in range(W-1, 0, -1):
        for k in range(n+1):
            if cnt[i][j][k]>=1:
                cnt[i][j-1][k] += cnt[i][j][k]
                
for i in range(W):
    for j in range(H-1, 0, -1):
        for k in range(n+1):
            if cnt[j][i][k]>=1: cnt[j-1][i][k]+=cnt[j][i][k]
            
for i in range(H-h+1):
    for j in range(W-w+1):
        for k in range(1, n+1):
            tmp = cnt[0][0][k]-cnt[i][j][k]+cnt[i+h][j][k]+cnt[i][j+w][k]-cnt[i+h][j+w][k]
            if tmp>=1: ans[i][j]+=1

for i in ans: print(*i)