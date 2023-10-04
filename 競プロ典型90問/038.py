"""
・ライブラリを使うやり方(Pythonなら通る)
"""
import math

a, b = map(int, input().split())
ans = math.lcm(a, b)
if ans>(10**18):
    print('Large')
else:
    print(ans)
    
    
# """
# ・別解
# """
# a, b = map(int, input().split())
# def gcd(a, b):
#     while b:
#         a, b = b, a%b
#     return a

# def lcm(a, b):
#     return (a*b) // gcd(a, b)

# ans = lcm(a, b)
# print('Large') if ans>10**18 else print(ans)