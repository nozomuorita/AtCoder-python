# 余弦定理
import math
a, b, h, m = map(int, input().split())

# 時針の角度(12の位置から)
th1 = (h*30) + (m*0.5)
# 分針の角度(12の位置から)
th2 = 6*m

theta = abs(th1-th2)
ans = (a**2) + (b**2) - (2*a*b*math.cos(math.radians(theta)))

print(ans**0.5)