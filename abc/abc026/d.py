from bisect import bisect_left, bisect_right, insort_left, insort_right
from math import sin, pi

a, b, c = map(int, input().split())
left, right = 0, 200

while 1:
    mid = (right+left) / 2
    ft = (a * mid) + (b * sin(c*mid*pi))
    if abs(ft-100)<(10**-9):
        break
    if ft>=100:
        right = mid
    else:
        left = mid
    
print(mid)