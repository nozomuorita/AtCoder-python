a, b = map(int, input().split())
ans = 0
for i in range(a, b+1):
    j = list(str(i))[::-1]
    if list(str(i))==j: ans += 1
    
print(ans)