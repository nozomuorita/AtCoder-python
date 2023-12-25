def ceil_div(x, y): return -(-x//y)
a, m, l, r = map(int, input().split())

s1 = ceil_div(l-a, m)
s2 = (r-a)//m

print(s2-s1+1)