import itertools

N, M = map(int, input().split())
k = []
x = []
for i in range(M):
    tmp = list(map(int, input().split()))
    k.append(tmp[0])
    x.append(tmp[1:])
    
list_ = [i for i in range(1, N+1)]
tmp = itertools.combinations(list_, 2)

ans = True
for i in tmp:
    flag = False
    i = list(i)
    for j in x:
        if (i[0] in j) and (i[1] in j):
            flag = True
            break
            
    if flag:
        continue
    else:
        ans = False
        break
        
if ans:
    print('Yes')
else:
    print('No')