H, W = map(int, input().split())
R, C = map(int, input().split())

ans = 0
for i, j in [[R+1, C], [R-1, C], [R, C+1], [R, C-1]]:
    if (1<=i<=H) and (1<=j<=W):
        ans += 1

print(ans)