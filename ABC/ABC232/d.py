h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
#print(c)
# dp[i][j]: マス(i, j)に到達するまでに通ることのできる最大のマス数
dp = [[0]*w for _ in range(h)]
dp[0][0] = 1

for i in range(h):
    for j in range(w):
        if c[i][j]=='#':
            continue
        f1, f2 = 0, 0
        if (0<=i-1<=h-1):
            f1 = dp[i-1][j]
        if (0<=j-1<=w-1):
            f2 = dp[i][j-1]
        mx = max(f1, f2)
        if mx != 0:
            dp[i][j] = max(f1, f2) + 1
            
ans = -1
for i in dp:
    mx = max(i)
    if mx>ans:
        ans = mx
#print(dp)
print(ans)