n = int(input())
l, r = [], []

for i in range(n):
    l_, r_ = map(int, input().split())
    l.append(l_)
    r.append(r_)

ans = 0
for i in range(n):
    ans += r[i] - l[i] + 1

print(ans)