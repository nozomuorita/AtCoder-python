N, Q = map(int, input().split())

L = []
a = []
for i in range(N):
    La = list(map(int, input().split()))
    L_tmp = La[0]
    a_tmp = La[1:]
    L.append(L_tmp)
    a.append(a_tmp)
    
for i in range(Q):
    s, t = map(int, input().split())
    print(a[s-1][t-1])