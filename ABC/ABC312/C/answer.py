from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 二分探索をするためソートする必要がある
a.sort()
b.sort()

# ansとなりうるのは、A_i か (B_i)+1 である
# そのためそれらの値をまとめたリストを作る
c = a.copy()
for i in b:
    c.append(i+1)
c = list(set(c)) # 一度set型にして重複をなくす
c.sort()

# 答えになりうる値について一つずつ確認
for i in c:
    # i円で売りたい人数は、右側挿入時のインデックス
    num_n = bisect_right(a, i)
    # i円で買いたい人は、左側挿入時インデックスをmから引いたもの
    num_m = m - bisect_left(b, i)
    
    # 売りたい人数のほうが大きいなら答え
    if num_n >= num_m:
        ans = i
        break

print(ans)