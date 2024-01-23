n, k = map(int, input().split())
a = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(n)]

# lightを持っている人
light = [False]*n
for i in a: light[i-1]=True

ans = -1
for i in range(n):
    if light[i]: continue
    score = float("inf")
    
    for j in range(n):
        if i==j or light[j]==False: continue
        score = min(score, (((xy[i][0] - xy[j][0])**2) + ((xy[i][1] - xy[j][1])**2)) ** 0.5)
    ans = max(ans, score)

print(ans)