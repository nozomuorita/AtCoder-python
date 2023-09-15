n = int(input())

k = []
for i in range(n):
    t, l, r = map(int, input().split())
    if t==1:
        k.append([l, r])
    elif t==2:
        k.append([l, r-0.1])
    elif t==3:
        k.append([l+0.1, r])
    else:
        k.append([l+0.1, r-0.1])
        
ans = 0
for i in range(n):
    for j in range(i+1, n):
        #print(i, j)
        k1, k2 = k[i], k[j]
        #print(k1, k2)
        if (k1[1]<k2[0]) or (k2[1]<k1[0]):
            continue
        else:
            ans += 1
            
print(ans)