from math import sin, cos, radians

n = int(input())
xy1 = list(map(int, input().split()))
x0 = xy1[0]
y0 = xy1[1]
xy2 = list(map(int, input().split()))

# 中心点
x = (xy1[0] + xy2[0]) / 2
y = (xy1[1] + xy2[1]) / 2
xy = [x, y]

# n角形の中心角
deg = radians(360/n)

x0 -= x
y0 -= y

ans_x = x0 * cos(deg) - y0 * sin(deg)
ans_y = x0 * sin(deg) + y0 * cos(deg)

ans_x += x
ans_y += y
print(ans_x, ans_y)
