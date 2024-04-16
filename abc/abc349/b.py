from collections import defaultdict
s = input()
d = defaultdict(set)

for i in s:
    score = s.count(i)
    d[score].add(i)

for key in list(d.keys()):
    if len(d[key])!=0 and len(d[key])!=2:
        exit(print('No'))

print('Yes')