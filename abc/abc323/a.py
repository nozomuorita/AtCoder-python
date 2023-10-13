s = input()

f = True
for i in range(1, 16, 2):
    if s[i]!='0':
        f = False
        break
    
if f:
    print('Yes')
else:
    print('No')