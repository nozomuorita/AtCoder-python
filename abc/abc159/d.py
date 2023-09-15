from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for i in range(n):
    d[a[i]] += 1

num = 0
for key in list(d.keys()):
    tmp = d[key]
    num += (tmp * (tmp-1)) // 2

for i in a:
    tmp = num
    tmp -= (d[i] * (d[i]-1)) // 2
    tmp += ((d[i]-1) * (d[i]-2)) // 2
    print(tmp)