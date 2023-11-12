a = [list(map(int, input().split())) for i in range(9)]

# 1
for i in range(9):
    if len(set(a[i]))==9: continue
    else: exit(print('No'))
    
# 2
for i in range(9):
    t = []
    for j in range(9): t.append(a[j][i])
    if len(set(t))==9: continue
    else: exit(print('No'))
    
# 3
for i in range(3):
    for j in range(3):
        t = []
        for k in range(3):
            for l in range(3):
                t.append(a[3*i+k][3*j+l])
        if len(set(t))==9: continue
        else: exit(print('No'))
        
print('Yes')