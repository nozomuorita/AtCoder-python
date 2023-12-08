from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for i in a:
    d[i] += 1

for key in list(d.keys()):
    if d[key]!=4: exit(print(key))