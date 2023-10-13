n = int(input())
lr = []
for i in range(n):
    _ = list(map(int, input().split()))
    lr.append(_)

lr.sort()

ans = []
for i in range(n):
    if len(ans)==0:
        ans.append(lr[i])
    else:
        if ans[-1][1]<lr[i][0]:
            ans.append(lr[i])
        else:
            if ans[-1][-1]>=lr[i][1]:
                continue
            else:
                ans[-1][1] = lr[i][1]

for i in ans:
    print(*i)