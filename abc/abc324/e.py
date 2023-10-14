"""
・各文字列について、前から作れる部分列と後ろから作れる部分列を事前計算する
・サンプル１について
・前から作れる部分列はS1=2文字、S2=1文字、S3=0文字である
・後ろから作れる部分列はS1=0文字、S2=1文字、S3=2文字である
・S1について、前からは2文字作れるので、後ろから1文字以上作れる文字列であれば全体としてTを作ることができる
・後ろから1文字以上作ることができるのは、S2とS3であるので2パターン
・S2について、前からは1文字作ることができるので、後ろから2文字以上作れる文字列であればOk
・よって、S3を結合すると作れる(+1)
・S3については前から0文字なので、後ろから3文字作れる文字列を結合する必要があるが、そのような文字列はないので、S3を先頭にして作ることはできない
・以上から、サンプル1の答えは2+1=3とすることができる。
・後ろから、〇文字以上作ることのできる文字列の数は累積和を計算し、二分探索で求めることで高速化
"""

from collections import defaultdict
from bisect import bisect_left, bisect_right, insort_left, insort_right

n, t = map(str, input().split())
n = int(n)
s = [input() for _ in range(n)]

# 各文字列がtの先頭から何文字目までつくれるか
d1 = defaultdict(int)
for i in range(n):
    idx = 0
    for j in range(len(s[i])):
        if s[i][j]==t[idx]:
            idx += 1
        if idx==len(t): break                 #  もし、インデックスがtの文字数を超えるならbreak(すべての文字を作ることができる)
    d1[i] = idx                               #  key: 文字列sの番号、value: 何文字目まで作れるか
    
# 各文字列がtの後ろから何文字目まで作れるか
# key文字分だけ作れる
d2 = defaultdict(list)
for i in range(n):
    idx = len(t)-1
    for j in reversed(range(len(s[i]))):      #  文字列sを後ろから見ていく  
        if s[i][j]==t[idx]:
            idx -= 1
        if idx==-1: break                     #  もし、インデックスが-1になるならbreak(tのすべての文字を作ることができる)
    
    d2[len(t)-(idx+1)].append(i)              #  key: 後ろから作ることのできる文字数、value: 文字列sの番号

# 後ろから作ることのできる文字数をkeysに入れ、ソート
keys = list(d2.keys())
keys.sort()

# 累積和を辞書で計算
# key: 文字数、value: 文字列の数
# 後ろからkey文字以上作ることのできる文字列の数が値(value)になる
d3 = defaultdict(int)
num = 0
for key in reversed(keys):
    d3[key] += num+len(d2[key])
    num += len(d2[key])

ans = 0
length = len(t)

# 各文字列を先頭にして作ることのできる組み合わせを計算
for i in range(n):
    tmp = d1[i]                           #  文字列iが先頭から作ることのできる文字数
    key = length - tmp                    #  後ろから作る必要のある文字数(tの文字数 - 文字列iで作れる文字数)
    idx = bisect_left(keys, key)          #  作る必要のある文字数(key)以上である累積和のkeyを二分探索

    if idx>=len(keys): continue           #  もし、二分探索で探したものがkeysの最大値より多いなら作ることはできないので飛ばす
    idx2 = keys[idx]                      #  keysのidx番目の値が累積和辞書d3にあるkey(d3[key]個だけ作れる(d3[key]はkey文字以上作ることのできる文字列の数))
    ans += d3[idx2]
    
print(ans)