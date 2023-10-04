from collections import deque
n, q = map(int, input().split())
a = deque(map(int, input().split()))

for i in range(q):
    t, x, y = list(map(int, input().split()))
    if t==1:
        a[x-1], a[y-1] = a[y-1], a[x-1]
    elif t==2:
        z = a.pop()
        a.appendleft(z)
    elif t==3:
        print(a[x-1])