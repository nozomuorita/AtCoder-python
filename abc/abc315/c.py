n = int(input())
fs = []
for i in range(n):
    f, s = map(int, input().split())
    fs.append((s, f))

fs.sort(reverse=True)
s1, f1 = fs[0]
ans = -1
for i in range(1, n):
    s2, f2 = fs[i]
    if f1==f2: ans=max(ans, s1+(s2//2))
    else: ans=max(ans, s1+s2)

print(ans)