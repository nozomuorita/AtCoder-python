n, k = map(int, input().split())
drag = 0
ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])
    drag += b

if drag<=k: exit(print(1))

ab.sort()
for i in range(n):
    drag -= ab[i][1]
    if drag<=k: print(ab[i][0]+1); break