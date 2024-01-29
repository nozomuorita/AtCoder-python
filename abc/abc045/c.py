from itertools import combinations
s = input()

ans = int(s)          # プラス記号を入れない場合だけansに
# i個プラス記号を入れる
for i in range(1, len(s)):
    c = combinations(range(len(s)-1), i)
    for j in c:
        score = 0
        idx = 0
        for k in j:
            score += int(s[idx:k+1])
            idx = k+1
        score += int(s[idx:])
        ans += score

print(ans)