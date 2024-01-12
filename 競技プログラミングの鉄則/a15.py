n = int(input())
a = list(map(int, input().split()))
a2 = sorted(list(set(a)))

d = {}
for i in range(len(a2)):
    d[a2[i]] = i+1

for i in range(n):
    print(d[a[i]], end=" ")