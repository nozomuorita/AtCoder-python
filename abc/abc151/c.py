from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(lambda: [0, 0])

for i in range(m):
    p, s = map(str, input().split())
    p = int(p)
    
    if d[p][0]>0:
        continue
    if s=='AC':
        d[p][0] += 1
    else:
        d[p][1] += 1
    
ac, wa = 0, 0
for i in range(1, n+1):
    ac += d[i][0]
    if d[i][0]>0:
        wa += d[i][1]
    
print(ac, wa)