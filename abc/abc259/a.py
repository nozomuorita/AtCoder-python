N, M, X, T, D = map(int, input().split())
n = N
ans = T

while (n != M):
    if n > X:
        ans = ans
    else:
        ans -= D
    
    n -= 1
    
print(ans)