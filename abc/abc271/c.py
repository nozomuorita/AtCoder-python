"""
・二分探索で読める冊数を探す
・読める冊数の上限はn+1冊であるため左端を0、右端をn+1として二分探索
・mid(mid巻まで読めるかどうか)に対して、for i in aとして以下の操作を行う
・もし、iがまだ読んでないものでmidより小さいならs(set型)に追加
・そうでない(mid巻より大きいかすでに読んだ巻(重複している))ならcnt(取り替えて読む本の候補)をインクリメント
・for文を回した後で最終的に読める冊数を計算
・s(普通に読む巻)とcnt(交換して読む冊数(2冊で交換できるので2で割った商))の和がmidより大きいなら読むことができる
・判定結果により左か右をずらす
"""

n = int(input())
a = list(map(int, input().split()))

ok = 0
ng = n + 1
while ng - ok > 1:
    mid = (ok + ng) // 2
    s = set()
    cnt = 0
    for i in a:
        if i <= mid and i not in s:
            s.add(i)
        else:
            cnt += 1
    if len(s) + (cnt // 2) >= mid:   #  読むことのできる冊数がmidより大きいなら
        ok = mid
    else:
        ng = mid

print(ok)