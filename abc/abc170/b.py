x, y = map(int, input().split())
if y % 2 != 0:
    print('No')
    exit()

if (y - 2*x)>=0 and (4*x - y)>=0:
    print('Yes')
else:
    print('No')