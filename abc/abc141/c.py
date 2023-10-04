"""
・それぞれの人が正解した数をカウントすることで計算量を削減
・まず初めにqがkよりも小さいなら1問も正解できなくても残るので、全員Yesとなる
・それ以外の場合については以下のようになる
・ある人iがm問正解したとする。
・するとq問(全部の問題数)のうちq-m問は不正解であるため、もともとのポイントkからq-mだけ引かれたものが最終的な得点と計算できる
・これが1以上なら生き残り、そうでないなら脱落と判定できる
"""

from collections import defaultdict
n, k, q = map(int, input().split())
d = defaultdict(int)

for i in range(q):
    a = int(input())
    d[a] += 1
    
if k>q:
    for i in range(n): print('Yes')
else:
    for i in range(1, n+1):
        if k-(q-d[i])>0:
            print('Yes')
        else:
            print('No')