n = int(input())
a = [int(input()) for _ in range(n)]

a2 = sorted(a, reverse=True)
mx1, mx2 = a2[0], a2[1]

if mx1==mx2:
    for i in range(n): print(mx1)
else:
    for i in range(n):
        if a[i]==mx1: print(mx2)
        else: print(mx1)