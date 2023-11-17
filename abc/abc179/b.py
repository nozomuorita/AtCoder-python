n = int(input())
d = [list(map(int, input().split())) for i in range(n)]

m = 0
for i in range(n):
    if len(set(d[i]))==1:
        m += 1
    else:
        m = 0
    
    if m==3:
        print('Yes')
        exit()
        
print('No')