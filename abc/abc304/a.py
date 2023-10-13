N = int(input())
S = []
A = []
for i in range(N):
    s, a = map(str, input().split())
    S.append(s)
    A.append(int(a))
    
a = 10000000000
min_i = 1000
for i in range(N):
    if A[i] < a:
        min_i = i
        a = A[i]
        
ans1 = S[min_i:]
ans2 = S[:min_i]

ans1.extend(ans2)
for i in range(N):
    print(ans1[i])