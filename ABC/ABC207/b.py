def ceil_div(x, y): return -(-x//y)

a, b, c, d = map(int, input().split())
tmp = 0
if (c*d-b)!=0:
    tmp = a / (c*d-b)
if tmp<0 or (c*d-b==0):
    print(-1)
else:
    print(ceil_div(a, c*d-b))