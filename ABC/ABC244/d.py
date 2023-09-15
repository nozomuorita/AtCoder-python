s = list(map(str, input().split()))
t = list(map(str, input().split()))

n = 0
for i in range(len(s)):
    if s[i] != t[i]:
        n += 1
        
if n==2:
    print('No')
else:
    print('Yes')