from collections import defaultdict
n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(1, n):
        d[i][j] += d[i][j-1]
for i in range(n):
    for j in range(1, n):
        d[j][i] += d[j-1][i]

d.insert(0, [0]*(n+1))
for i in range(1, n+1):
    d[i].insert(0, 0)

mx = [0]*(n*n+9)
for i in range(1, n+1):
    for j in range(i, n+1):
        for k in range(1, n+1):
            for l in range(k, n+1):
                score = d[j][l] - d[i-1][l] - d[j][k-1] + d[i-1][k-1]
                num = (j-i+1) * (l-k+1)
                mx[num] = max(mx[num], score)

for i in range(1, len(mx)):
    mx[i] = max(mx[i-1], mx[i])
    
q = int(input())
for i in range(q):
    p = int(input())
    print(mx[p])