# 次数が３以上の頂点があるとだめ
from collections import defaultdict
ab = defaultdict(int)
for i in range(3):
    a, b = map(int, input().split())
    ab[a] += 1
    ab[b] += 1
    
for i in list(ab.keys()):
    if ab[i]==3:
        print('NO')
        exit()
        
print('YES')