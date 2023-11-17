n = int(input())
ans = 0

for i in range(1, n):
    t = (n-1)//i
    ans += t

print(ans)