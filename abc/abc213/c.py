"""
・座圧
"""
from collections import defaultdict

h, w, n = map(int, input().split())
a, b = [], []
for i in range(n):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)

row = defaultdict(int)
col = defaultdict(int)
a2 = sorted(list(set(a)))
b2 = sorted(list(set(b)))

for i in range(len(a2)):
    row[a2[i]] = i+1
for i in range(len(b2)):
    col[b2[i]] = i+1
    
for i in range(n):
    print(row[a[i]], col[b[i]])