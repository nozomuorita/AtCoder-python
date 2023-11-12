from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for i in range(n):
    d[a[i]] = i+1
    
for key in sorted(list(d.keys())):
    print(d[key], end=' ')