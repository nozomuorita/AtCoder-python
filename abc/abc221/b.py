s = list(input())
t = list(input())

if s==t:
    print('Yes')
    exit()

for i in range(len(s)-1):
    tmp = s.copy()
    tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
    if tmp == t:
        print('Yes')
        exit()
        
print('No')