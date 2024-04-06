def ceil_div(x, y): return -(-x//y)
n = int(input())
p = list(map(int, input().split()))

ans = 0
score = 0
for i in range(n):
    if p[i]==(i+1):
        score += 1
    else:
        ans += ceil_div(score, 2)
        score = 0

ans += ceil_div(score, 2)
print(ans)