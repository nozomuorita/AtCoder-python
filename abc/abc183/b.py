sx, sy, gx, gy = map(int, input().split())

ans = (sx*gy + sy*gx) / (sy + gy)
print(ans)