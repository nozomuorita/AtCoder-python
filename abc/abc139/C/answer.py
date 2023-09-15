n = int(input())
h = list(map(int, input().split()))

# チェック済みの要素を管理
checked = [False] * n
checked[0] = True
ans = 0
s = 0

for i in range(1, n):
    # すでにチェックしているなら飛ばす
    if checked[i]:
        continue
    checked[i] = True
    if h[i]<=h[i-1]:
        s += 1
    else:
        ans = max(ans, s)
        s = 0
    
ans = max(ans, s)
print(ans)