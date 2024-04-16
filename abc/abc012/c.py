n = int(input())
kuku = 0
for i in range(1, 10):
    for j in range(1, 10):
        kuku += i*j

d = kuku - n
ans = []
for i in range(1, 10):
    for j in range(1, 10):
        if i*j==d:
            ans.append([i, j])

ans.sort()
for i in range(len(ans)):
    print(ans[i][0], "x", ans[i][1])