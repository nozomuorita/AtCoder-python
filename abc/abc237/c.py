s = list(input())
s_r = list(reversed(s))

a1, a2 = 0, 0
f1, f2 = True, True
for i in range(len(s)):
    if (s[i] == 'a') and (f1):
        a1 += 1
    if (s_r[i] == 'a') and (f2):
        a2 += 1
        
    if s[i] != 'a':
        f1 = False
    if s_r[i] != 'a':
        f2 = False
        
if a1 > a2:
    print('No')
    exit()
elif a1 == a2:
    print('Yes') if s==s_r else print('No')
else:
    k = a2 - a1
    s = s[:len(s)-k]
    s_r = s_r[k:]
    
    print('Yes') if s==s_r else print('No')