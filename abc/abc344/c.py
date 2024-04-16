from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
l = int(input())
c = list(map(int, input().split()))
q = int(input())
x = list(map(int, input().split()))

d = defaultdict(lambda: False)

for i in range(n):
    for j in range(m):
        for k in range(l):
            score = a[i]+b[j]+c[k]
            d[score] = True

for i in range(q):
    if d[x[i]]: print('Yes')
    else: print('No')