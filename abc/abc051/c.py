sx, sy, gx, gy = map(int, input().split())
ans = ""

ans += "U" * (gy-sy)
ans += "R" * (gx-sx)
ans += "D" * (gy-sy)
ans += "L" * (gx-sx)

ans += "L"

ans += "U" * (gy-sy+1)
ans += "R" * (gx-sx+1)

ans += "DR"

ans += "D" * (gy-sy+1)
ans += "L" * (gx-sx+1)
ans += "U"

print(ans)