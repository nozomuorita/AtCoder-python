n, m = map(int, input().split())
s = [input() for _ in range(n)]

ans = float("inf")
for i in range(2**n):
    num = 0
    pop = [False]*m
    for j in range(n):
        if i>>j & 1:
            num += 1
            for k in range(m):
                if s[j][k]=="o":
                    pop[k] = True
    
    if all(pop):
        ans = min(ans, num)

print(ans)