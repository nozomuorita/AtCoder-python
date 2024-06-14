n = int(input())
a = list(map(int, input().split()))

a.sort()
d = []

for i in range(1, n):
    tmp = a[i] - a[i-1]
    d.append(tmp)
