def ceil_div(x, y): return -(-x//y)

h = int(input())
w = int(input())
n = int(input())

mx = max(h, w)
ans = ceil_div(n, mx)
print(ans)
