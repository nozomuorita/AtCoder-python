n = int(input())
a = list(map(int, input().split()))

l1 = [] # odd
l2 = [] # even

for i in range(len(a)):
    if (i+1)%2==0:
        l2.append(a[i])
    else:
        l1.append(a[i])

if n%2==0:
    l2 = list(reversed(l2))
    print(*l2, *l1)
else:
    l1 = list(reversed(l1))
    print(*l1, *l2)