n, m = map(int, input().split())
s = [input()[-3:] for _ in range(n)]
t = [input() for _ in range(m)]

ans = 0
for i in s:
    if i in t: ans+=1
print(ans)