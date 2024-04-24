n, m = map(int, input().split())

d1 = 6*m
d2 = 30*n + 0.5*m

d = (max(d1, d2) - min(d1, d2)) % 360
print(min(d, 360-d))