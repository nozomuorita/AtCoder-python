n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

for i in range(n-m+1):
    for j in range(n-m+1):
        if a[i][j]!=b[0][0]: continue
        
        ok = True
        for k in range(m):
            for l in range(m):
                if (0<=i+k<n) and (0<=j+l<n) and (a[i+k][j+l]==b[k][l]): continue
                ok = False
        
        if ok: exit(print('Yes'))

print('No')