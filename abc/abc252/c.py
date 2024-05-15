n = int(input())
s = []
for i in range(n):
    s.append(input())

ans = float("inf")
# 数字iを止める
for i in range(10):
    idx = [0]*10
    for j in range(n):
        k = s[j].index(str(i))
        idx[k] += 1
    
    score = 0
    for j in range(10):
        score = max(score, j+(idx[j]-1)*10)
    
    ans = min(ans, score)

print(ans)