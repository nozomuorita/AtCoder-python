n = int(input())
a = list(map(int, input().split()))
st = [list(map(int, input().split())) for _ in range(n-1)]

for i in range(n-1):
    x = a[i]//st[i][0]
    a[i] -= st[i][0]*x
    a[i+1] += st[i][1]*x
        
print(a[-1])