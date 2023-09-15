n = int(input())
a = list(map(int, input().split()))
ans = -1

for i in range(n):
    first = a[i]
    mn = first
    for j in range(i, n):
        if a[j]<mn:
            mn = a[j]
        num = mn * (j-i+1)
    
        if num>ans:
            ans = num
            
print(ans)