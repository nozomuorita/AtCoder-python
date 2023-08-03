s = input()

for i in range(len(s)):
    # even
    if ((i+1)%2==0):
        if not(s[i].isupper()):
            print('No')
            exit()
    # odd
    else:
        if not(s[i].islower()):
            print('No')
            exit()

print('Yes')