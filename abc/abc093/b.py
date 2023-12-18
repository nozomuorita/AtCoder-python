a, b, k = map(int, input().split())
ans = []
for i in range(a, a+k):
    if a<=i<=b: ans.append(i)
for i in range(b-k+1, b+1):
    if a<=i<=b: ans.append(i)
ans = list(set(ans))
ans.sort()
for i in ans: print(i)
