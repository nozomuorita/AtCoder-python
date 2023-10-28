N = int(input())
S = input()
flag = False

for i in S:
    if i=='|':
        flag = not(flag)
        
    elif i=='*':
        if flag:
            ans = 'in'
        else:
            ans = 'out'
            
print(ans)