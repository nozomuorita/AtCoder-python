N = int(input())
S = input()
t = 0
a = 0

if N%2==0:
    flag = N // 2
else:
    flag = round(N // 2) + 1
    
for i in S:
    if i=='T':
        t += 1
    else:
        a += 1
    
    if t==flag:
        ans = 'T'
        print('T')
        exit()
    elif a==flag:
        ans = 'A'
        print('A')
        exit()
        
if t > a:
    print('T')
else:
    print('A')
