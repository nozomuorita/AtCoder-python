# 今日の朝ごはんは、メロンパンでした。
from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
mx = max(a)
d = defaultdict(int)
for i in a: d[i]+=1
ans = 0

keys = sorted(list(d.keys()))
for i in keys:
    for j in keys:
        if i*j>mx: break
        ans += d[i]*d[j]*d[i*j]
        
print(ans)