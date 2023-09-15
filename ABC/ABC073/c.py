from collections import defaultdict
n = int(input())
a = [int(input()) for i in range(n)]

d = defaultdict(int)
for i in range(n):
    if d[a[i]] > 0:
        d[a[i]] -= 1
    else:
        d[a[i]] += 1
    
    if d[a[i]] == 0:
        del d[a[i]]
        
print(len(list(d.keys())))