n = int(input())
p = list(map(int, input().split()))

ans = 0
l = []
mn = 10**10
for i in range(n):
    if p[i] < mn: ans += 1
    l.append(p[i])
    if mn > p[i]: mn = p[i]

print(ans)