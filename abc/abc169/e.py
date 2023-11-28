n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

mn, mx = [], []
for i in range(n):
    mn.append(ab[i][0])
    mx.append(ab[i][1])
mn.sort()
mx.sort()

if n%2==0:
    mnm = mn[n//2] + mn[(n//2)-1]
    mxm = mx[n//2] + mx[(n//2)-1]
    print(mxm-mnm+1)
else:
    mnm = mn[(n-1)//2]
    mxm = mx[(n-1)//2]
    print(mxm-mnm+1)