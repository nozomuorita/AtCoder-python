from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)

for i in range(n):
    d[a[i]-1] += 1
    d[a[i]] += 1
    d[a[i]+1] += 1
    
ans = 0
for key in list(d.keys()):
    if d[key] > ans:
        ans = d[key]
        
print(ans)