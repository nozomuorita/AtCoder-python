N = int(input())
X = list(map(int, input().split()))
ans = 1000000000

for i in range(1, max(X)+1):
    tmp = 0
    for j in X:
        tmp += (j - i) ** 2
        
    ans = min(tmp, ans)
    
print(ans)