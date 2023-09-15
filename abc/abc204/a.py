x, y = map(int, input().split())

if len(set([x, y]))==2:
    if x+y==1:
        print(2)
    elif x+y==2:
        print(1)
    else:
        print(0)
        
else:
    print(x)