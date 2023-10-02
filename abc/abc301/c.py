from collections import defaultdict
s = list(input())
t = list(input())

ds = defaultdict(int)
dt = defaultdict(int)
s_a, t_a = 0, 0

for i in range(len(s)):
    if s[i]=='@':
        s_a += 1
    else:
        ds[s[i]] += 1
    if t[i]=='@':
        t_a += 1
    else:
        dt[t[i]] += 1

keys = set(list(ds.keys()) + list(dt.keys()))
for i in keys:
    if ds[i] == dt[i]:
        continue
    elif ds[i] < dt[i]:
        if (i in 'atcoder') and (s_a>=(dt[i]-ds[i])):
            s_a -= (ds[i]-dt[i])
        else:
            print('No')
            exit()
    else:
        if (i in 'atcoder') and (t_a>=(ds[i]-dt[i])):
            t_a -= (dt[i]-ds[i])
        else:
            print('No')
            exit()

print('Yes')