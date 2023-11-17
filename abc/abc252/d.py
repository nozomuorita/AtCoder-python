from collections import defaultdict
n = int(input())
a  =list(map(int, input().split()))

d = defaultdict(int)
for i in a: d[i]+=1

keys = sorted(d.keys())
d2 = defaultdict(int)
for i in range(len(keys)):
    if i==0: d2[keys[i]]=0
    else: d2[keys[i]]=d2[keys[i-1]]+d[keys[i-1]]
    
ans = 0
for i in range(n):
    small = d2[a[i]]
    big = n-small-d[a[i]]
    
    ans += small*big

print(ans)