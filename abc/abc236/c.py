from collections import defaultdict
n, m = map(int, input().split())
s = list(map(str, input().split()))
t = list(map(str, input().split()))

d = defaultdict(lambda: False)
for i in t: d[i]=True

for i in s:
    print('Yes') if d[i] else print('No')