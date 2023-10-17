"""
・いもす法
"""
from collections import defaultdict
n, w = map(int, input().split())
d1 = defaultdict(int)

for i in range(n):
    s, t, p = map(int, input().split())
    d1[s] += p
    d1[t] -= p

keys = sorted(list(d1.keys()))    
d2 = defaultdict(int)
d2[keys[0]] = d1[keys[0]]
for i in range(1, len(keys)):
    d2[keys[i]] = d2[keys[i-1]] + d1[keys[i]]
    
for i in list(d2.keys()):
    if d2[i]>w:
        print('No')
        exit()
    
print('Yes')

# n,w = map(int,input().split())
# l = 2 * (10**5)+1
# v = [0] * l

# for i in range(n):
#   s,t,p = map(int,input().split())
#   v[s] += p
#   v[t] -= p

# for i in range(l-1):
#   v[i+1] += v[i]

# if (max(v) > w):
#   print('No')
# else:
#   print('Yes')
