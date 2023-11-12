from collections import defaultdict
n, x = map(int, input().split())
a = list(map(int, input().split()))
d = defaultdict(int)
for i in range(n):
    d[a[i]] += 1
    
for i in list(set(a)):
    aj = i-x
    if d[aj]>0: exit(print('Yes'))
    
print('No')