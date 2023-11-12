n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(n)]

ans = 0
for i in range(n):
    t = 0
    for j in range(m): t+=(a[i][j]*b[j])
    t += c
    if t>0: ans+=1
    
print(ans)