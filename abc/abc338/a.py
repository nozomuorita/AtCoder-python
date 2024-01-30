s = input()

if not(s[0].isupper()): exit(print('No'))

for i in s[1:]:
    if not(i.islower()): exit(print('No'))

print('Yes')