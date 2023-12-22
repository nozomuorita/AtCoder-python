def ceil_div(x, y): return -(-x//y)
h, w = map(int, input().split())

if h==1 or w==1: exit(print(1))

col = ceil_div(h, 2)
row = ceil_div(w, 2)
ans = col*row
ans += (h-col)*(w-row)
print(ans)