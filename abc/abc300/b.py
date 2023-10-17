H, W = map(int, input().split())
A, B = [], []

for i in range(H):
    a = input()
    A.append(a)
for i in range(H):
    b = input()
    B.append(b)
    
def s_shift(A):
    tmp = A[0]
    A = A[1:]
    A.append(tmp)
    
    return A

def t_shift(A):
    new_A = []
    for i in range(H):
        a = A[i]
        tmp = a[0]
        a = a[1:]
        a += tmp
        
        new_A.append(a)
        
    return new_A

for s in range(H):
    for t in range(W):
        tmp_A = A.copy()
        
        for i in range(s):
            tmp_A = s_shift(tmp_A)
        for i in range(t):
            tmp_A = t_shift(tmp_A)
            
        if tmp_A == B:
            print('Yes')
            exit()
            
print('No')