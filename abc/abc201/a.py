A = list(map(int, input().split()))

# A1, A2, A3のそれぞれの差(3パターン)のうち、2つが一致しているなら可能
a12 = abs(A[0]-A[1])
a23 = abs(A[1]-A[2])
a13 = abs(A[0]-A[2])

if (a12==a13) or (a12==a23) or (a23==a13):
    if len(set(A))==2:
        print('No')
    else:
        print('Yes')
else:
    print('No')