from collections import defaultdict

n, k = map(int, input().split())
d = defaultdict(int)
for i in range(k):
    dt = int(input())
    a = list(map(int, input().split()))
    for j in a:
        d[j] += 1
        
ans = 0
for i in range(1, n+1):
    if d[i] == 0:
        ans += 1
        
print(ans)