"""
・bit全探索で赤色に変える行、列を選択して書き換えたときの「#」の数を数える
・赤色に書き換える行の選択肢は行数をhとして2**h通りである
・ex)h=2のとき
・00ならどれも選択しない
・01なら1行目のみ選択
・10なら2行目のみ選択
・11なら1,2行目を選択
・列も同様に考え、書き換える列を選択
・書き換えたら、#の数を数え、ちょうどkならansをインクリメント
・行、列数が最大6なので最大でも(2**6)*(2**6)ほどで間に合いそう
"""

from copy import deepcopy
h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]
ans = 0

for i in range(2**h):
    for j in range(2**w):
        c2 = deepcopy(c)
        # row
        for t in range(h):
            if (i>>t) & 1:
                c2[t] = ['r'] * w  # 赤色"r"で書き換え
        
        # col
        for t in range(w):
            if (j>>t) & 1:
                for r in range(h):
                    c2[r][t] = 'r'  # 赤色"r"で書き換え
        
        # count
        s = 0
        for t in c2:
            s += t.count('#')
        if s==k:
            ans += 1
            
print(ans)