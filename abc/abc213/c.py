from collections import defaultdict
h, w, n = map(int, input().split())

col = []
row = []
a, b = [], []
d_row = defaultdict(int)
d_col = defaultdict(int)

for i in range(n):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)
    row.append(a_)
    col.append(b_)
    
row.sort()
col.sort()
r_set = set()
c_set = set()

r, c = 1, 1
for i in range(n):
    if row[i] not in r_set:
        d_row[row[i]] = r
    if col[i] not in c_set:
        d_col[col[i]] = c
    if row[i] not in r_set:
        r += 1
        r_set.add(row[i])
    if col[i] not in c_set:
        c += 1
        c_set.add(col[i])
    
for i in range(n):
    ans_r = d_row[a[i]]
    ans_c = d_col[b[i]]
    print(ans_r, ans_c)