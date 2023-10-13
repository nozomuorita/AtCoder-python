h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]

ans = 0
for i in range(h-1):
    for j in range(w-1):
        n = b[i][j]-a[i][j]
        if n!=0:
            a[i][j] += n
            a[i+1][j] += n
            a[i+1][j+1] += n
            a[i][j+1] += n
            ans += abs(n)
        
if a==b:
    print('Yes')
    print(ans)
else:
    print('No')