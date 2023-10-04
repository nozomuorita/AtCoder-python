"""
・優先度付きキュー
・貪欲に高いものから1枚ずつ割引券を使用していく
・最初、ansには割引券を使わない合計金額を入れておく
・次に割引券を1枚ずつ使用していく(while文)
・優先度付きキューから最大値を取り出し、割引券を1枚使った場合の割引額をansから引く
・割引券を1枚使ったあとの金額を再びキューに入れる
・残りの割引券枚数を1枚引く
"""

from heapq import heapify, heappop, heappush
n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 0   # 最小金額(初期値は割引券を使わない場合の合計金額)
a2 = []
for i in range(n): 
    ans+=a[i]
    a2.append(-a[i])
    
heapify(a2)   # 優先度付きキューに変換

#  割引券が残っている間、繰り返す
while m>0:
    mx = -heappop(a2)       # 最大値を取り出す
    ans -= mx-(mx//2)       # 割り引かれる金額をansから引く
    m -= 1                  # 残りの割引券の枚数を引く
    heappush(a2, -(mx//2))  # 割引券使用後の金額を再びキューへ追加
    
print(ans)