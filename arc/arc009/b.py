b = list(map(str, input().split()))
n = int(input())
a = [input() for _ in range(n)]

d = {}
lst = []
for i in range(n):
    number = ""
    for j in range(len(a[i])):
        number += str(b.index(a[i][j]))
    d[int(number)] = a[i]
    lst.append(int(number))

keys = sorted(lst)
for key in keys:
    print(d[key])