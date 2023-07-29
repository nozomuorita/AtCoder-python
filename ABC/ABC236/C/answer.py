from collections import defaultdict

n, m = map(int, input().split())
S = list(map(str, input().split()))
T = list(map(str, input().split()))

# 特急停車駅をdictに格納
d = defaultdict(lambda: False)
for i in range(m):
    d[T[i]] = True

for i in range(n):
    s = S[i]
    
    if d[s]:
        print('Yes')
    else:
        print('No')