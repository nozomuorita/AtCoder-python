n, s, k = map(int, input().split())
pq = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    ans += pq[i][0]*pq[i][1]

if ans>=s: ans+=k
print(ans)