n = input()

if len(n)==1:
    print('Yes')
    exit()

for i in range(len(n)-1):
    if n[i] > n[i+1]:
        continue
    else:
        print('No')
        exit()
        
print('Yes')