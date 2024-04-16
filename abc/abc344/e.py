from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

d = defaultdict(lambda: [-1, -1])
if n==1:
    d[a[0]] = ["h", "t"]
else:
    for i in range(n):
        if i==0:
            d[a[i]] = ["h", a[1]]
        elif i==(n-1):
            d[a[i]] = [a[-2], "t"]
        else:
            d[a[i]] = [a[i-1], a[i+1]]

q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0]==1:
        x, y = map(int, query[1:])
        if d[x][1]!="t":
            d[y] = [x, d[x][1]]
            d[d[x][1]][0] = y
            d[x][1] = y
        else:
            d[y] = [x, "t"]
            d[x] = [d[x][0], y]
    else:
        x = query[1]
        pre = d[x][0]
        now = x
        pos = d[x][1]
        
        if d[now][0]=="h":
            d[d[now][1]][0] = "h"
            d[now] = [-1, -1]
        elif d[now][1]=="t":
            d[d[now][0]][1] = "t"
            d[now] = [-1, -1]
        else:
            d[pre][1] = d[now][1]
            d[pos][0] = d[now][0]

for key in list(d.keys()):
    if d[key][0]=="h":
        idx = key
        break
ans = [idx]
while 1:
    if d[idx][1]=="t": break
    
    idx = d[idx][1]
    ans.append(idx)

print(*ans)