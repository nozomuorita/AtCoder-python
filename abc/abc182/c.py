n = list(input())

ans = 100
for i in range(2**len(n)):
    t = ''
    dn = 0
    for j in range(len(n)):
        if i>>j & 1: dn+=1
        else: t+=n[j]
    if len(t)==0: continue
    if int(t)%3==0: ans=min(ans, dn)
    
print(ans) if ans!=100 else print(-1)