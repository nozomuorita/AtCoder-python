n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
a = [(a[i], -(i+1)) for i in range(n)]
b = list(map(int, input().split()))
b = [(b[i], -(i+1)) for i in range(n)]
c = [(a[i][0]+b[i][0], -(i+1)) for i in range(n)]

ans = []
a.sort(reverse=True)
for i in range(x):
    ans.append(-a[i][1])
b.sort(reverse=True)
cnt = 0
for i in range(n):
    if cnt==y:
        break
    if -b[i][1] not in ans:
        ans.append(-b[i][1])
        cnt += 1
c.sort(reverse=True)
cnt = 0
for i in range(n):
    if cnt==z:
        break
    if -c[i][1] not in ans:
        ans.append(-c[i][1])
        cnt += 1

for i in sorted(ans): print(i)