n = int(input())
a = list(map(int, input().split()))

deg = set([0, 360])
cut = 0
for i in range(n):
    cut += a[i]
    cut %=360
    deg.add(cut)

deg = sorted(list(deg))
ans = 0
for i in range(len(deg)-1):
    ans = max(ans, deg[i+1]-deg[i])
print(ans)