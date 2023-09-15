n = int(input())
p = [int(input()) for i in range(n)]

mx = max(p)
ans = sum(p)
ans -= mx//2
print(ans)