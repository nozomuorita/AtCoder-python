from collections import defaultdict
from decimal import Decimal
N = int(input())
ans = defaultdict(list)
    
for i in range(N):
    a, b = map(int, input().split())
    tmp = Decimal(a) / (Decimal(a)+Decimal(b))
    ans[tmp].append(i+1)

keys = sorted(list(ans.keys()), reverse=True)    

for i in keys:
    tmp2 = sorted(ans[i])
    for j in tmp2:
        print(j, end=' ')