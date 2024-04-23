n, k = map(int, input().split())

# 出た目がk以上である場合(その時点で勝ち)
ans = max(0, n-k+1)/n

# 出た目がk未満ならば、k以上になるまで(1/2)を引く必要がある
for i in range(1, n+1):
    if i>=k: break
    score = i
    num = 0
    while score<k:
        score *= 2
        num += 1
    ans += (1/n) * ((1/2)**num)

print(ans)