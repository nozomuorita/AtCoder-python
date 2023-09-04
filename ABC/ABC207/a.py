num = list(map(int, input().split()))
ans = -1

for i in range(3):
    for j in range(i+1, 3):
        tmp = num[i] + num[j]
        ans = max(ans, tmp)
        
print(ans)