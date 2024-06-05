n, m, k = map(int, input().split())
lst = []
for i in range(m):
    lst.append(list(map(str, input().split())))

ans = 0

for i in range(2**n):
    keys = [False]*n
    for j in range(n):
        if i>>j & 1:
            keys[j] = True

    f = True
    for j in range(m):
        cnt = 0
        for l in lst[j][1:int(lst[j][0])+1]:
            if keys[int(l)-1]:
                cnt += 1
                if cnt>=k: break
        
        if cnt>=k:
            if lst[j][-1]=="o": continue
            else:
                f = False
                break
        else:
            if lst[j][-1]=="x": continue
            else:
                f = False
                break
    
    if f: ans+=1
    
print(ans)
    
    