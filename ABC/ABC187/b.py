n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(i+1, n):
        xy1, xy2 = xy[i], xy[j]
        if (xy2[0]-xy1[0])==0:
            k = 0
        else:
            k = (xy2[1]-xy1[1]) / (xy2[0]-xy1[0])
        if -1<=k<=1:
            ans += 1
            
print(ans)