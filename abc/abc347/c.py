n, a, b = map(int, input().split())
d = list(map(int, input().split()))

r = set()
for i in d:
    r.add(i%(a+b))

if len(r)==1:
    if a>=1: exit(print('Yes'))
    else: exit(print('No'))

r = sorted(list(r))
k = []
for i in range(len(r)-1):
    k.append(r[i+1]-r[i]-1)
k.append(r[0]+(a+b)-r[-1]-1)

ans = (a+b) - max(k)
if ans<=a: print('Yes')
else: print('No')