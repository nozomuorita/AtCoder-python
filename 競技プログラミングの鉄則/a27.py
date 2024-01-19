"""mathライブラリ"""
from math import gcd
a, b = map(int, input().split())
ans = gcd(a, b)
print(ans)