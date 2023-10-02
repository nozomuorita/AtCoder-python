import math
a, b, c = map(int, input().split())

# 最大公約数
g = math.gcd(a, b)
g = math.gcd(g, c)

ans = 0
for i in [a, b, c]:
    ans += (i//g) - 1

print(ans)