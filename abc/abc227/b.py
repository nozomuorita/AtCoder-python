n=int(input())
s=list(map(int, input().split()))
ans=0

for i in range(n):
    si=s[i]
    f = False

    for a in range(1, si+1):
        for b in range(1, si+1):
            if (4*a*b+3*a+3*b)==si:
                f = True
    
    if f:
        continue
    else:
        ans+=1

print(ans)