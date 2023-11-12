r, g, b, n = map(int, input().split())

ans = 0
for i in range(3001):
    for j in range(3001):
        boll = (r*i) + (g*j)
        if boll>n: break
        
        blue = n-boll
        if blue%b==0: ans+=1
        
print(ans)