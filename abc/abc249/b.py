S = list(input())

up = False
low = False

for i in S:
    if ord('A') <= ord(i) <= ord('Z'):
        up = True
    if ord('a') <= ord(i) <= ord('z'):
        low = True
        
if up and low:
    l_origin = len(S)
    S_set = set(S)
    if len(S_set) == l_origin:
        print('Yes')
    else:
        print('No')
    
else:
    print('No')