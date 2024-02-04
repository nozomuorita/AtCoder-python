"""
・女子の組合せを全探索
・各女子について、それぞれの男子へのzを事前に管理(defaultdict(lambda: defaultdict(int)))
・ある組合せについて、選んだ女子が与える幸福度をmaleに足す(male[i]: i番目の男子が選んだ女子からもらえる幸福度)
・maleには選んだ女子により各男子がもらえる幸福度が入っている
・maleの大きいほうからq人選んで和をとったものがその女子の組み合わせでのスコア
"""
from itertools import combinations
from collections import defaultdict
n, m, p, q, r = map(int, input().split())
d = defaultdict(lambda: defaultdict(int))
for i in range(r):
    x, y, z = map(int, input().split())
    d[x][y] += z

ans = 0
c = combinations(range(1, n+1), p)
for i in c:
    male = [0]*(m+1)
    for j in i:
        for key in list(d[j].keys()):
            male[key] += d[j][key]
    
    score = sum(sorted(male, reverse=True)[:q])
    ans = max(ans, score)

print(ans)