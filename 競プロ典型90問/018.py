"""
・Xの解説参照
"""

from math import sin,  cos, radians, atan2, degrees
t = int(input())
l, X, Y = map(int, input().split())
q = int(input())

for i in range(q):
    e = int(input())
    x = 0
    y = -(l/2)*sin(radians(360*(e/t)))
    z = (l/2)-(l/2)*cos(radians(360*(e/t)))
    
    v = z  # 垂直距離
    h = ((X-x)**2 + (Y-y)**2)**0.5  # 水平距離
    ans = atan2(v, h)
    ans = degrees(ans)
    print(ans)