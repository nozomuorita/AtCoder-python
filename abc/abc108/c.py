from collections import defaultdict
n, k = map(int, input().split())
ans = 0

d = defaultdict(int)
for i in range(1, n+1):
    d[i%k] += 1

for i in range(1, n+1):
    rb = i%k    
    t =(k-rb)%k
    if (t+t)%k==0:
        ans += d[t]*d[t]
    
print(ans)