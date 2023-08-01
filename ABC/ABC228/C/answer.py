# 4日目において、自分だけ300点で、他の人が0点であるときにk位以内であれば、可能性がある
import bisect

n, k = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]

# 3日目までの合計点
s = []
for i in range(n):
    s.append(sum(p[i]))

# ソート
s_sort = sorted(s)

for i in range(n):
    score = s[i]
    index = bisect.bisect_right(s_sort, score+300)

    if n-index < k:
        print('Yes')
    else:
        print('No')

# ==================================================================================
# # 別解(二分探索を用いない)
# # 3日目終了時点で、上位k番目の人の点数をk_scoreとおく
# # それぞれの人において、3日目終了時の点数+300がk_score以上ならYesとなる

# n, k = map(int, input().split())
# p = [list(map(int, input().split())) for _ in range(n)]

# # 3日目までの合計点
# s = []
# for i in range(n):
#     s.append(sum(p[i]))

# # 高い順にソート
# s_sort = sorted(s, reverse=True)
# # k番目の人の点数を取得
# k_score = s_sort[k-1]

# for i in range(n):
#     score = s[i] + 300
#     if score >= k_score:
#         print('Yes')
#     else:
#         print('No')