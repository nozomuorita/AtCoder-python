s = input()
num = [str(i).zfill(3) for i in range(1, 350)]
if s[:3]=="ABC" and (s[3:] in num):
    if s[3:]!="316":
        exit(print('Yes'))

print('No')