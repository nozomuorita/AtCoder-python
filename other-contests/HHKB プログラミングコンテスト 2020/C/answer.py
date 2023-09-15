n = int(input())
p = list(map(int, input().split()))

# dp[i]: p1...piのいずれとも等しくない値の中での最小値
dp = [-1] * n
# 初期値
dp[0] = 1 if p[0]==0 else 0
appeared = [False]*200001
appeared[p[0]] = True

for i in range(1, n):
    if not appeared[p[i]]:
        appeared[p[i]] = True
    if p[i]!=dp[i-1]:
        dp[i] = dp[i-1]
    else:
        for j in range(dp[i-1], len(appeared)):
            if appeared[j]:
                continue
            else:
                dp[i] = j
                break
    #print(dp)
for i in dp:
    print(i)        