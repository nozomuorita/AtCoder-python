n = int(input())
sc = []
sum_ = 0
for i in range(n):
    s, c = map(str, input().split())
    sc.append([s, int(c)])
    sum_ += int(c)

sc.sort()
ans = sc[sum_%n][0]
print(ans)