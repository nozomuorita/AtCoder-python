n = int(input())
ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append([b-a, a, b])

ab.sort()

ans = 0
for i in range(n-1):
    ans += ab[i][1]
ans += ab[-1][2]
print(ans)