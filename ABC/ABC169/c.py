from decimal import Decimal

a, b = map(Decimal, input().split())
b *= 100
ans = a * b
ans /= 100
print(int(ans))