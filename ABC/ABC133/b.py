n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(i+1, n):
        tmp = 0
        x1 = x[i]
        x2 = x[j]
        
        for k in range(d):
            tmp += (x1[k] - x2[k]) ** 2
        tmp = tmp ** 0.5
        if tmp.is_integer():
            ans += 1
            
print(ans)