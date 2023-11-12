from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
mod = 10**9+7

d = defaultdict(int)
for i in range(n):
    d[a[i]] += 1
    
# odd
if n%2!=0:
    for key in list(d.keys()):
        if key==0 and d[key]!=1: exit(print(0))
        elif key!=0 and key%2==0 and d[key]!=2: exit(print(0))
        elif key%2!=0: exit(print(0))
        
    ans = pow(2, n//2, mod)
# even
else:
    for key in list(d.keys()):
        if key%2==0: exit(print(0))
        elif key%2!=0 and d[key]!=2: exit(print(0))
    
    ans = pow(2, n//2, mod)

print(ans)