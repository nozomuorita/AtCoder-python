N = int(input())
W = list(map(str, input().split()))
flag = ['and', 'not', 'the', 'that', 'you']

for i in W:
    if i in flag:
        print('Yes')
        exit()
        
print('No')