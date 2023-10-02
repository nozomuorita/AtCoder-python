def ceil_div(x, y): return -(-x//y)
a, b, c, d = map(int, input().split())

takahashi = ceil_div(c, b)
aoki = ceil_div(a, d)

if takahashi <= aoki:
    print('Yes')
else:
    print('No')