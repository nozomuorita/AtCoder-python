A, B = map(int, input().split())
no = [[3, 4], [4, 3], [6, 7], [7, 6]]

if (abs(A-B)==1):
    if [A, B] not in no:
        print('Yes')
    else:
        print('No')
else:
    print('No')