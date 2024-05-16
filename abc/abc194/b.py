n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

ans = float("inf")
for i in range(n):
    for j in range(n):
        if i==j: ans=min(ans, sum(ab[i]))
        else:
            ans = min(ans, max(ab[i][0], ab[j][1]))

print(ans)