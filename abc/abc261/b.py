N = int(input())
A = []
for i in range(N):
    a = input()
    A.append(a)
    
for i in range(N):
    for j in range(i+1):
        if i == j:
            continue
        
        if A[i][j] == 'W':
            if A[j][i] == 'L':
                continue
            else:
                print('incorrect')
                exit()
                
        elif A[i][j] == 'L':
            if A[j][i] == 'W':
                continue
            else:
                print('incorrect')
                exit()
        elif A[i][j] == 'D':
            if A[j][i] == 'D':
                continue
            else:
                print('incorrect')
                exit()
                
print('correct')