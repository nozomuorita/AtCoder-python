S = list(map(int, input().split()))

tmp = -1
for i in S:
    if (i>=tmp) and (100<=i<=675) and (i%25==0):
        tmp = i
        continue
    else:
        print('No')
        exit()
        
print('Yes')