from math import sin, cos, radians
a, b, d = map(int, input().split())

# 原点なら変わらない
if (a==0) and (b==0):
    print(0, 0)
    exit()

r = (a**2 + b**2)**0.5 # 半径

cos_theta = a/r
sin_theta = b/r
cos_d = cos(radians(d))
sin_d = sin(radians(d))

x = r * (cos_theta*cos_d - sin_theta*sin_d)
y = r * (sin_theta*cos_d + cos_theta*sin_d)

print(x, y)