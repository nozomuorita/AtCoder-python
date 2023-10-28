from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
ans = 0

for i in range(n):
    j = i
    t = (j+1) - a[j]
    t2 = (i+1) + a[i]
    ans += d[t]
    d[t2] += 1
    
print(ans)