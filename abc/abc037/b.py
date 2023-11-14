n, q = map(int, input().split())
lst = [0]*n

for i in range(q):
    l, r, t = list(map(int, input().split()))
    for j in range(l-1, r):
        lst[j] = t
        
for i in lst: print(i)