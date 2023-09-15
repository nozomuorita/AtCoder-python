s = input()
s_r = s[::-1]

if s != s_r:
    print('No')
    exit()

s2 = s[:(len(s)-1)//2]
s2_r = s2[::-1]
if s2 != s2_r:
    print('No')
    exit()
    
s3 = s[(len(s)+3)//2-1:]
s3_r = s3[::-1]
if s3 != s3_r:
    print('No')
    exit()
    
print('Yes')