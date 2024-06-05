n, k = map(int, input().split())
a = list(map(int, input().split()))
idx = []
for i in range(n):
    idx.append([a[i], i])
idx.sort()

c = k//n
k -= (k//n) * n
ans = [c]*n

for i in range(k):
    ans[idx[i][1]] += 1

for i in ans: print(i)