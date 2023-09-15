"""
・二分探索
・SortedListを用いる(本来はMultisetぽい)
・クエリ１：SoetedListライブラリを用いて、要素を追加する
・bisectを使ってリストに挿入すると、TLEしてしまう
・クエリ２，３：要素xを二分探索し、そのインデックスからk個ずれた場所の要素が答え
・k個ずれた場所がリスト外なら-1
"""
from sortedcontainers import SortedList
# https://qiita.com/shogo314/items/0d61b18a034a6bd1ce08

q = int(input())
a = SortedList()

l = 0
for i in range(q):
    query = list(map(int, input().split()))
    if query[0]==1:
        a.add(query[1])
        l += 1
        
    elif query[0]==2:
        x = query[1]
        k = query[2]
        
        idx = a.bisect_right(x)
        idx -= 1
        print(a[idx-(k-1)]) if 0<=idx-(k-1)<l else print(-1)   
            
    else:
        x = query[1]
        k = query[2]
        
        idx = a.bisect_left(x)
        print(a[idx+k-1]) if 0<=idx+k-1<l else print(-1)