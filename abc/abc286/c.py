"""
・全探索
・ローテ1回のとき、ローテ2回のときでのかかる金額を計算
・置き換えは、s[i]とs[n-i-1]を見て、異なるなら片方を変える必要がある
"""
n, a, b = map(int, input().split())
s = list(input())

ans = float("inf")
for i in range(n):
    score = 0
    for j in range(n//2):
        if s[j]!=s[n-1-j]: score+=1
    
    ans = min(ans, a*i+b*score)
    s = s[1:] + [s[0]]
    
print(ans)