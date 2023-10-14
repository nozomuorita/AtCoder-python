"""
・包除原理で求める。
・答えとなるのは、(a~bまでの個数)-(cまたはdで割り切れるもの)である。
・(cまたはdで割り切れるもの)=(cで割り切れるもの)+(dで割り切れるもの)-(cでもdでも割り切れるもの)である。
・これを計算して求める。
"""

from math import lcm
def ceil_div(x, y): return -(-x//y)
a, b, c, d = map(int, input().split())

#  a~bまでの個数
n1 = b-a+1

# cで割り切れるもの
t1 = ceil_div(a, c)
t2 = b//c
n2 = t2-t1+1

# dで割り切れるもの
t1 = ceil_div(a, d)
t2 = b//d
n3 = t2-t1+1

# cでもdでも割り切れるもの
l = lcm(c, d)
t1 = ceil_div(a, l)
t2 = b//l
n4 = t2-t1+1

# cまたはdで割り切れるもの
n5 = n2+n3-n4

ans = n1-n5
print(ans)