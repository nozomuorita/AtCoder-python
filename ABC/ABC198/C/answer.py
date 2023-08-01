r, x, y = map(int, input().split())

# 原点と(x, y)のユークリッド距離を計算
dist = ((x**2) + (y**2)) ** 0.5

if dist == r:
    print(1)
elif dist <= 2*r:
    print(2)
else:
    print(int(-(-dist//r)))