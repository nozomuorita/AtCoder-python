n = int(input())

s = n//1000

if (n-s*1000)==0:
    print(0)
else:
    print(1000-(n-s*1000))