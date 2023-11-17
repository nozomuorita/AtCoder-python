N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

m = max(A)
list_ = []  # 食べる可能性のある食べ物の番号
for i in range(len(A)):
    if A[i] == m:
        list_.append(i+1)
        
flag = False
for i in list_:
    if i in B:
        flag = True
        break
        
if flag:
    print('Yes')
else:
    print('No')