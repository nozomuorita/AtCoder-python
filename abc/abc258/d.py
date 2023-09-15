# 最適な行動は、どれか一つのステージを何度も繰り返しプレイすること(クリアにかかる時間が短いものをやり続ければ最小となる)
# 1番目のステージを繰り返す場合、2番目のステージを繰り返す場合...としてnだけfor文を回す

inf = float('inf')

n, x = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab_s = [ab[0][0]+ab[0][1]]
for i in range(1, n):
    ab_s.append(ab_s[i-1] + ab[i][0] + ab[i][1])

ans = inf
# i番目を何回もプレイする
for i in range(n):
    t = ab_s[i]
    m = x - (i + 1)
    if m < 0:
        continue
    t += m * ab[i][1]
    
    if t < ans:
        ans = t
        
print(ans)