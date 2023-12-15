n, m = map(int, input().split())
times = 100*(n-m) + 1900*m
ans = times*(pow(2, m))
print(ans)
