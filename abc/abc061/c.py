from collections import defaultdict

n, k = map(int, input().split())
d = defaultdict(int)
for i in range(n):
    a, b = map(int, input().split())
    d[a] += b
    
keys = sorted(list(d.keys()))
    
for key in keys:
    k -= d[key]
    if k<=0: print(key); exit()