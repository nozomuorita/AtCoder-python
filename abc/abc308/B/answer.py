N, M = map(int, input().split())
C = list(map(str, input().split()))
D = list(map(str, input().split()))
P = list(map(int, input().split()))

ans = 0

for i in range(N):
    eat = C[i]
    num = -100
    for j in range(len(D)):
        if eat == D[j]:
            num = j
    
    if num == -100:
        ans += P[0]
    else:
        ans += P[num+1]
print(ans)