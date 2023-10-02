# ok
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
q = int(input())

d = defaultdict(int)
s = 0
for i in range(n):
    d[a[i]] += 1
    s += a[i]

for i in range(q):
    b, c = map(int, input().split())
    num = d[b]
    
    s -= b*num
    s += c*num
    
    d[b] -= num
    d[c] += num
    
    print(s)