l, r = map(int, input().split())
ans = []
num = l
idx = 0
while 1:
    for i in range(60, -1, -1):
        if num==0:
            if (((2**i)*(1))<=(r)):
                ans.append([num, (2**i)*1])
                num = (2**i)*1
                if num==r:
                    print(len(ans))
                    for j in ans:
                        print(*j)
                    exit()
                break
        else:
            if ((2**i)<=num) and (num%(2**i)==0) and (((2**i)*(num//(2**i)+1))<=(r)):
                ans.append([num, (2**i)*(num//(2**i)+1)])
                num = (2**i)*(num//(2**i)+1)
                if num==r:
                    print(len(ans))
                    for j in ans:
                        print(*j)
                    exit()
                break