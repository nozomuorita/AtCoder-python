n = int(input())
z, w = [], []
for i in range(n):
    x, y = map(int, input().split())
    z.append(x+y)
    w.append(x-y)

ans = max(max(z)-min(z), max(w)-min(w))
print(ans)