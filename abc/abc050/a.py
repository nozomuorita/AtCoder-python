l = list(map(str, input().split()))

if l[1]=='+':
    print(int(l[0])+int(l[2]))
else:
    print(int(l[0])-int(l[2]))