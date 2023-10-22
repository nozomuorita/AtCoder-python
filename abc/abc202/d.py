"""
・先頭から決めていく
"""
from math import comb
a, b, k = map(int, input().split())
ans = ""

while a>0 and b>0:
    c = comb(a+b-1, a-1)
    if k<=c:
        ans += "a"
        a -= 1
    else:
        ans += "b"
        b -= 1
        k -= c

ans += "a"*a + "b"*b
print(ans)