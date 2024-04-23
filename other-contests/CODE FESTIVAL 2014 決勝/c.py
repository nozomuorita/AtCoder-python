a = int(input())

for i in range(10, 10001):
    score = 0
    p = 1
    for j in reversed(str(i)):
        score += p*int(j)
        p *= i
    
    if score==a:
        exit(print(i))

print(-1)