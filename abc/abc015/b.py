def ceil_div(x, y): return -(-x//y)
n = int(input())
a = list(map(int, input().split()))

s = sum(a)
l = n-a.count(0)
ans = ceil_div(s, l)
print(ans)