n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(101):
    a2 = a.copy()
    a2.append(i)
    a2.sort()
    s = sum(a2[1: -1])
    if s >= x:
        print(i)
        exit()
        
print(-1)