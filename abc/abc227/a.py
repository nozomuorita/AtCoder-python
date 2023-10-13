N, K, A = map(int, input().split())

ans = (A+K-1) % N
print(ans if ans!=0 else N)