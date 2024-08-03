xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())

d1 = ((xa-xb)**2 + (ya-yb)**2)
d2 = ((xa-xc)**2 + (ya-yc)**2)
d3 = ((xb-xc)**2 + (yb-yc)**2)

d = sorted([d1, d2, d3])

if (d[0] + d[1])==d[2]:
    print('Yes')
else:
    print('No')