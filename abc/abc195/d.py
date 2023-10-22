"""
・二分探索(二分探索なしでもいけるっぽい)
・価値の大きい荷物を入れることのできる一番小さい箱に入れていくと最適
・各クエリでの処理
・LからRまでの箱を除いたリストx2を作る
・x2から重さwを二分探索し、wを入れることのできる最小の箱(インデックス)を探す
・そのインデックスがまだ使われていない(used[idx]=False)ならその箱に入れる(used[idx]=Trueとし、ansに価値を足す)
・もし、使われているならインデックスをずらし、一つずつ大きな箱を見ていく(最後までないなら入れることはできない)
・これをすべての荷物について行い、答えを出力
"""

from bisect import bisect_left, bisect_right, insort_left, insort_right

n, m, q = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(n)]
WV.sort(reverse=True, key=lambda x: x[1])

x = list(map(int, input().split()))

for _ in range(q):
    l, r = map(lambda x: x-1, map(int, input().split()))
    x2 = sorted(x[:l] + x[r+1:])                         #  L~Rまでの箱を取り除き、最大重量が小さい順でソート
    
    used = [False]*len(x2)                               #  すでに箱を使ったかどうか
    ans = 0
    
    for w, v in WV:
        idx = bisect_left(x2, w)                         #  重さwの荷物を入れることができる最小の箱のインデックスを取得
        if idx==len(x2): continue                        #  もし、すべての箱について入れることができないなら飛ばす
        while idx!=len(x2) and used[idx]==True: idx+=1   #  すでに使われているなら次に大きい箱を使うとする、一番大きい箱まで到達したら終了
        if idx==len(x2): continue                        #  idx==len(x2)の場合、すべての箱について入れることができないので飛ばす
        used[idx] = True                                 #  箱を使用中にして、答えに価値を追加
        ans += v
        
    print(ans)