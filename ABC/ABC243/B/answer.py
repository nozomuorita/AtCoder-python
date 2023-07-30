n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = a.copy()
c.extend(b)
c = list(set(c))

ans1 = 0
ans2 = 0

for i in c:
    if (i in a) and (i in b):
        if a.index(i) == b.index(i):
            ans1 += 1
        else:
            ans2 += 1
            
print(ans1)
print(ans2)