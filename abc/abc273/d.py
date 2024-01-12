"""
・辞書に各行・各列にあるブロックの列・行を入れる
・row[i]: i行目にあるブロックの列番号リスト(ソートする)
・col[i]: i列目にあるブロックの行番号リスト(ソートする)
・以降、高橋くんは座標(R, C)にいるとする
・d=="L"の場合
・高橋くんはR行目を左に移動する
・R行目にブロックがない(row[R]が空)ならば、自由に移動できる
・高橋くんは、C-lまで移動できる。ただし、枠外にはいってはいけない
・ゆえに移動後は、max(0, C-l)となる
・row[R]が空でないなら、row[R]からC(高橋くんがいる列)を二分探索する(idxを得る)
・idx==0なら、高橋くんより左にブロックはないので自由に移動できる
・ゆえに、max(0, C-l)になる
・idx!=0なら、高橋くんの左にブロックが存在する
・高橋くんより左にあって、最も近いブロックはrow[R][idx-1]である。
・lだけ移動するまでにこのブロックにぶつかるならそこまで移動するし、lだけ移動してもそのブロックに当たらないならlだけ移動できる
・ゆえに、高橋くんの移動後の列番号はmax(row[R][idx-1]+1, C-l)となる

・d="R"の場合
・Lの場合と逆に考える
・row[R]が空なら自由に移動できる→min(w-1, C+l)
・違えば、二分探索
・idx==len(row[R])ならば、高橋くんより右にブロックは存在しない。
・ゆえに自由に移動できる→min(w-1, C+l)
・それ以外なら高橋くんより右にブロックが存在→ブロックにぶつかるか、lだけ移動するまで動ける
・→min(row[R][idx]-1, C+l)
・d="U", d="D"も同様。
"""
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict
h, w, rs, cs = map(int, input().split())
n = int(input())
takahashi = [rs-1, cs-1]

row, col = defaultdict(list), defaultdict(list)
for i in range(n):
    r, c = map(lambda x: x-1, map(int, input().split()))
    row[r].append(c)
    col[c].append(r)

for key in list(row.keys()):
    row[key] = sorted(row[key])
for key in list(col.keys()):
    col[key] = sorted(col[key])

q = int(input())
for _ in range(q):
    d, l = map(str, input().split())
    l = int(l)
    takahashi_row = takahashi[0]
    takahashi_col = takahashi[1]
    
    if d=="L":
        tmp = row[takahashi_row]
        if len(tmp)==0: takahashi[1]=max(0, takahashi_col-l)
        else:
            idx = bisect_left(tmp, takahashi_col)
            if idx==0:
                takahashi[1] = max(0, takahashi_col-l)
            else:
                takahashi[1] = max(tmp[idx-1]+1, takahashi_col-l)
    elif d=="R":
        tmp = row[takahashi_row]
        if len(tmp)==0: takahashi[1]=min(w-1, takahashi_col+l)
        else:
            idx = bisect_left(tmp, takahashi_col)
            if idx==len(tmp):
                takahashi[1] = min(w-1, takahashi_col+l)
            else:
                takahashi[1] = min(tmp[idx]-1, takahashi_col+l)
    elif d=="U":
        tmp = col[takahashi_col]
        if len(tmp)==0: takahashi[0]=max(0, takahashi_row-l)
        else:
            idx = bisect_left(tmp, takahashi_row)
            if idx==0:
                takahashi[0] = max(0, takahashi_row-l)
            else:
                takahashi[0] = max(tmp[idx-1]+1, takahashi_row-l)
    else:
        tmp = col[takahashi_col]
        if len(tmp)==0: takahashi[0]=min(h-1, takahashi_row+l)
        else:
            idx = bisect_left(tmp, takahashi_row)
            if idx==len(tmp):
                takahashi[0] = min(h-1, takahashi_row+l)
            else:
                takahashi[0] = min(tmp[idx]-1, takahashi_row+l)
        
    print(takahashi[0]+1, takahashi[1]+1)