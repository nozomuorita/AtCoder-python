# 解説AC
# max(n)=300なのでO(n^3)で大丈夫
# 三角形の面積の公式を用いる

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            x1, y1 = xy[i][0], xy[i][1]
            x2, y2 = xy[j][0], xy[j][1]
            x3, y3 = xy[k][0], xy[k][1]
            
            if abs((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)) != 0:
                ans += 1

print(ans)