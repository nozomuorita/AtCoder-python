from collections import defaultdict
n = int(input())
s = [input() for _ in range(n)]

ans = 10**18

# 数字iを揃える場合を考える
for i in range(10):
    d = defaultdict(int)
    for j in s:
        idx = j.index(str(i))
        d[idx] += 1
        
    mx, idx = 1, -1
    for key in list(d.keys()):
        if d[key]>mx: mx=d[key]; idx=key
        elif d[key]==mx and key>idx: idx=key
    
    if mx==1: ans=min(ans, idx)
    else:
        t = (mx-1)*10 + idx
        ans = min(ans, t)
        
print(ans)