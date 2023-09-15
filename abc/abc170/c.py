from collections import defaultdict

x, n = map(int, input().split())
p = list(map(int, input().split()))

d = defaultdict(lambda: False)
for i in range(n):
    d[p[i]] = True

for i in range(1000):
    if d[x-i] == False:
        print(x-i)
        exit()
    if d[x+i] == False:
        print(x+i)
        exit()