def ceil_div(x, y): return -(-x//y)

n, k = map(int, input().split())
if k <= ceil_div(n, 2):
    print('YES')
else:
    print('NO')