q = int(input())
a = []

for i in range(q):
    t, x = map(int, input().split())
    if t==1:
        a.insert(0, x)
    elif t==2:
        a.append(x)
    else:
        print(a[x-1])