from collections import defaultdict
n = int(input())
a = sorted(list(map(int, input().split())))

d = defaultdict(lambda: False)
ans = 0
for i in range(n):
    s = a[i]
    while s%2==0: s//=2
    
    if d[s]==False:
        ans += 1
        d[s] = True

print(ans)