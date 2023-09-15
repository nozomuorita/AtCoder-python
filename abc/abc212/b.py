x = list(input())
ans = 'Weak'

if len(set(x))==1:
    ans = 'Weak'
else:
    for i in range(len(x)-1):
        if int(x[i])==9:
            if int(x[i+1]) != 0:
                ans = 'Strong'
                break
        else:
            if int(x[i+1]) != int(x[i])+1:
                ans = 'Strong'
                break

print(ans)