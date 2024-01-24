n = int(input())
s, p = [], []
jinko = 0
for i in range(n):
    _ = list(map(str, input().split()))
    s.append(_[0]); p.append(int(_[1]))
    jinko += int(_[1])

half = jinko//2 + 1
ans = "atcoder"
for i in range(n):
    if p[i]>=half: ans=s[i]; break

print(ans)