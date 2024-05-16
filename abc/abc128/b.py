n = int(input())
d = {}
sp = []

for i in range(n):
    s, p = map(str, input().split())
    sp.append([s, -int(p)])
    d[(s, -int(p))] = i+1

sp.sort()
for i in range(n):
    print(d[tuple(sp[i])])