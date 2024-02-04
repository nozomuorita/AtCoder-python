n = int(input())
a = list(map(int, input().split()))

score = 0
hito = 0
for i in range(n):
    hito += -a[i]
    score = max(score, max(0, hito))

ans = sum(a) + score
print(ans)