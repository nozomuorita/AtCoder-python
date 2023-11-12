from collections import defaultdict
s = input()
d = defaultdict(lambda: 0)

t = [0]*10
ts = ''.join(map(lambda x: str(x), t))
d[ts] += 1

for i in s:
    num = int(i)
    t[num] += 1
    t[num] %= 2
    ts = ''.join(map(lambda x: str(x), t))
    d[ts] += 1
    
ans = 0
for key in list(d.keys()):
    ans += (d[key]*(d[key]-1))//2

print(ans)