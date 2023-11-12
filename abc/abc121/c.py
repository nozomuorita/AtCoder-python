n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort()

ans = 0
drink = 0

for i in range(n):
    a, b = ab[i][0], ab[i][1]
    x = min(m-drink, b)
    drink += x
    ans += a*x

    if drink==m: break
    
print(ans)