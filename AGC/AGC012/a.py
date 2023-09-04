n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
ans = 0
num = 0
for i in range(1, 3*n, 2):
    ans += a[i]
    num += 1
    if num==n:
        break
    
print(ans)