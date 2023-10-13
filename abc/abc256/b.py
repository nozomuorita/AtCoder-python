N = int(input())
A = list(map(int, input().split()))
P = 0

space = [0] * 4

for i in A:
    tmp = [0] * 4
    space[0] = 1
    for j in range(4):
        if space[j] == 1:
            if j + i >= 4:
                P += 1
            else:
                tmp[j + i] = 1
                
    space = tmp
    
print(P)