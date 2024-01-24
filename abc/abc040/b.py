n = int(input())
ans = float("inf")

for i in range(1, 10**6+1):
    s = n//i
    r = n%i
    score = abs(s-i) + r
    ans = min(ans, score)

print(ans)
