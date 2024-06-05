n, m = map(int, input().split())
a = list(map(int, input().split()))

x = [list(map(int, input().split())) for _ in range(n)]

eiyou = [0]*m

for i in range(n):
    for j in range(m):
        tmp = x[i][j]
        eiyou[j] += tmp

for i in range(m):
    if a[i]<=eiyou[i]:
        continue
    else:
        exit(print('No'))

print('Yes')