from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ad = defaultdict(int)
for i in range(n):
    ad[a[i]] += 1
ans = 0

for i in range(n):
    tmp = c[i]
    ans += ad[b[tmp-1]]

print(ans)