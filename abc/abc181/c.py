# 全探索
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            a, b, c = xy[i], xy[j], xy[k]
            if (b[0]-a[0])!=0:
                katamuki1 = (b[1]-a[1])/(b[0]-a[0])
            else:
                katamuki1 = float('inf')
            if (c[0]-b[0])!=0:
                katamuki2 = (c[1]-b[1])/(c[0]-b[0])
            else:
                katamuki2 = float('inf')
            
            if katamuki1==katamuki2:
                print('Yes')
                exit()
                
print('No')