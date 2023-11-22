n = int(input())
a = list(map(int, input().split()))
ans = 0

# 全探索
for i in range(n):
    mn = a[i]
    for j in range(i, n):
        if a[j]<mn: mn=a[j]
        score = mn * (j-i+1)
        ans = max(ans, score)
        
print(ans)