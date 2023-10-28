N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

if T in C:
    tmp = []  #いろがT
    tmp2 = []
    for i in range(len(C)):
        if C[i]==T:
            tmp.append(i)
            tmp2.append(R[i])
    
    ma = max(tmp2)
    ind = tmp2.index(ma)
    ans = tmp[ind] + 1
    
    
else:
    T = C[0]
    
    tmp = []  #いろがT
    tmp2 = []
    for i in range(len(C)):
        if C[i]==T:
            tmp.append(i)
            tmp2.append(R[i])
    
    ma = max(tmp2)
    ind = tmp2.index(ma)
    ans = tmp[ind] + 1
    
    
print(ans)