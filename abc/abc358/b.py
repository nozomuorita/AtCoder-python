n, a = map(int, input().split())
t = list(map(int, input().split()))

ti = 0
mati = 0
for i in range(n):
    if t[i]<ti:
        ti = ti + a
    else:
        ti = t[i]+a
    print(ti)