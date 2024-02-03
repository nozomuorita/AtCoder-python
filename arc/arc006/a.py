e = list(map(str, input().split()))
b = input()
l = list(map(str, input().split()))

bonus = False
same = 0
for i in range(6):
    if l[i] in e: same+=1
    elif l[i]==b[0]: bonus=True

if same==6: print(1)
elif same==5 and bonus: print(2)
elif same==5 and bonus==False: print(3)
elif same==4: print(4)
elif same==3: print(5)
else: print(0)