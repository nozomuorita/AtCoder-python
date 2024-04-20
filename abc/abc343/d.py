from collections import defaultdict
n, t = map(int, input().split())
d = defaultdict(int)
d[0] = n
score = [0]*n
ans = 1

for i in range(t):
    a, b = map(int, input().split())
    a -= 1
    d[score[a]] -= 1
    if d[score[a]]==0:
        ans -= 1
    d[score[a]+b] += 1
    if d[score[a]+b]==1:
        ans += 1
    score[a] += b
    print(ans)