n, a, b = map(int, input().split())

ans = []
f = True

for i in range(n*a):
    tmp = ''
    for j in range(n*b):
        if f:
            if (i//a)%2==0:
                if (j//b)%2==0:
                    tmp += '.'
                else:
                    tmp += '#'
            else:
                if (j//b)%2==0:
                    tmp += '.'
                else:
                    tmp += '#'
                    
        else:
            if (i//a)%2==0:
                if (j//b)%2==0:
                    tmp += '#'
                else:
                    tmp += '.'
            else:
                if (j//b)%2==0:
                    tmp += '#'
                else:
                    tmp += '.'
            
    ans.append(tmp)
    if i%a==a-1:
        f = not(f)

for i in ans:
    print(i)