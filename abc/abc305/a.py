n = int(input())

for i in range(5):
    if (n+i)<=100 and (n+i)%5==0: exit(print(n+i))
    elif (n-i)>=0 and (n-i)%5==0: exit(print(n-i))