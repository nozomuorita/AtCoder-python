A = list(map(int, input().split()))

ans = 0
for i in range(len(A)):
    tmp = A[i] * (2**i)
    ans += tmp

print(ans)