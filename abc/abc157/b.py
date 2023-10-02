A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))

A = [A1, A2, A3]
N = int(input())
b = [int(input()) for _ in range(N)]


# 開いた数字を0で置き換える
for i in b:
    for j in A:
        if i in j:
            for k in range(len(j)):
                if j[k]==i:
                    j[k] = 0

if (A[0][0]==0) and (A[0][1]==0) and (A[0][2]==0):
    print('Yes')
elif (A[1][0]==0) and (A[1][1]==0) and (A[1][2]==0):
    print('Yes')
elif (A[2][0]==0) and (A[2][1]==0) and (A[2][2]==0):
    print('Yes')
elif (A[0][0]==0) and (A[1][0]==0) and (A[2][0]==0):
    print('Yes')
elif (A[0][1]==0) and (A[1][1]==0) and (A[2][1]==0):
    print('Yes')
elif (A[0][2]==0) and (A[1][2]==0) and (A[2][2]==0):
    print('Yes')
elif (A[0][0]==0) and (A[1][1]==0) and (A[2][2]==0):
    print('Yes')
elif (A[0][2]==0) and (A[1][1]==0) and (A[2][0]==0):
    print('Yes')
else:
    print('No')