n = int(input())
d = list(map(int, input().split()))

ans = 0
for i in range(n):
    t = d[i]
    t2 = int(str(i+1)[0])
    if len(set(list(str(i+1))))!=1: continue
    
    if t2<=t: ans+=1
    if int(str(t2)+str(t2))<=t: ans+=1
            
print(ans)