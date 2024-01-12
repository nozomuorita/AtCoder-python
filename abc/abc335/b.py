n = int(input())
ans = []
for i in range(22):
    for j in range(22):
        for k in range(22):
            if i+j+k>n: continue
            ans.append([i, j, k])

ans.sort()
for i in ans:
    print(*i)