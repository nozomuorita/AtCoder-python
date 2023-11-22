from collections import defaultdict
n, m = map(int, input().split())
a = list(map(int, input().split()))

d = defaultdict(int)
tosen = 1
mx = 0
for i in range(m):
    d[a[i]] += 1
    if d[a[i]]>mx:
        mx = d[a[i]]
        tosen = a[i]
    elif d[a[i]]==mx:
        if a[i]<tosen: tosen = a[i]
    
    print(tosen)