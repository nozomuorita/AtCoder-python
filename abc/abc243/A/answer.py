V, A, B, C = map(int, input().split())
n = 1

while True:
    if V < A:
        print('F')
        exit()
    V -= A
    
    if V < B:
        print('M')
        exit()
    V -= B
    
    if V < C:
        print('T')
        exit()
    V -= C