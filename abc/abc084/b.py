a, b = map(int, input().split())
s = input()

for i in range(len(s)):
    if i<a or a<i:
        if s[i] not in "0123456789": exit(print('No'))
    elif i==a:
        if s[i]!="-": exit(print('No'))
    
print('Yes')