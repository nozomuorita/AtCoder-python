from collections import defaultdict
n = int(input())
s = input()
d = defaultdict(int)

if n==1: exit(print(1))

ch = 1
for i in range(1, n):
    if s[i]==s[i-1]: ch+=1
    else: ch=1
    d[s[i]] = max(d[s[i]], ch)
    
ans = sum(list(d.values()))
print(ans)