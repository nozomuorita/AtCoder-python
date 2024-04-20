n = int(input())
for i in range(n):
    ans = []
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j]==1:
            ans.append(j+1)
    print(*ans)