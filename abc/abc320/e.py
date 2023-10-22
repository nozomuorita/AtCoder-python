"""
・heapq
・各イベント(そうめんが流れる or 人が列に戻ってくる)を時刻順にheapqで管理
・列に並んでいる人を番号順にheapqで管理
・イベントを時刻順に一つずつ取り出す
・取り出したイベントが「そうめんが流れる」なら列の先頭にいる人を取り出し、その人にそうめんの量だけ足す
・そうめんをとった人に対して、t+s秒後に列に戻るというイベントをheapqに追加
・取り出したイベントが「人が列に戻る」なら、その人を並んでいる人のheapqに追加。
"""

from heapq import heapify, heappop, heappush

n, m = map(int, input().split())
q1 = [tuple(map(int, input().split())) for _ in range(m)]    #  そうめんが流れるイベント(tuple)
q2 = [i for i in range(1, n+1)]                              #  列に並んでいる人(最初は全員が番号順)
ans = [0]*(n+1)                                              #  各人が得たそうめんの量(index=0はダミー)
heapify(q1)
heapify(q2)

#  イベントを一つずつ取り出す
while q1:
    t, w, s = heappop(q1)
    if w>0:                             #  w>0、すなわちそうめんが流れるイベントならば
        if q2:                          #  q2が空でない(=列に誰か並んでいる)なら一人取り出してそうめんを得る
            v = heappop(q2)             #  列に並んでいる人の先頭を取り出す
            ans[v] += w                 #  その人にwだけそうめんを追加
            heappush(q1, (t+s, 0, v))   #  その人がt+s秒に戻ってくるとして、イベントを追加(そうめんが流れるイベントと区別するためにw=0とする(そうめんイベントはw>0なので))
    else:                               #  人が戻ってくるイベントなら
        heappush(q2, s)                 #  その人を並んでいる人の列(heapq)に追加
        
for i in range(1, len(ans)): print(ans[i])