def ceil_div(x, y): return -(-x//y)
n, x, t = map(int, input().split())
print(ceil_div(n, x) * t)