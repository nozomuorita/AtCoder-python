"""
・二分探索
・各ピースを始点としたときに、全体のちょうど10分の1となる場所が存在するかを二分探索で探す
・ちょうど10分の1となる区間がn個目のピースをまたいでも良いようにリストaを2回繰り返したものを用意して考える
・以下手順
・各ピースの長さaに関する累積和を計算しておく(このとき、長さ2*aとしてaを二回繰り返した累積和を計算)
・各切れ目(ピース1を始点としたとき、ピース2を始点としたとき...)について、その切れ目までの累積和を取得(m)
・その累積和に10分の1だけ足したもの(m+(s/10))が累積和上でのちょうど10分の1となる大きさ
・m+(s/10)を二分探索で探し、ちょうどその値が存在するならyesで終了
・すべての切れ目を始点として探しても見つからないなら、no
"""

from bisect import bisect_left, bisect_right, insort_left, insort_right
n = int(input())
a = list(map(int, input().split()))

# 累積和を計算(ピースnをまたいで計算できるように2倍の長さにする)
cum = [0]
for i in range(2*len(a)):
    cum.append(cum[-1]+a[i%len(a)])
s = sum(a)                              # aの総和

# 各切れ目について、ちょうど10分の1となる場所がそんざいするか判定
for i in range(n+1):
    t = cum[i]                          # 切れ目iまでの累積和
    m = cum[i] + (s/10)                 # 切れ目iからちょうど10分の1の長さとなる累積和
    idx = bisect_left(cum, m)           # 切れ目iからちょうど10分の1の長さとなる累積和を探索しインデックスを取得
    if cum[idx]-t==(int(s/10)):         # 探索した場所がちょうど10分の1となっていれば存在することになる
        print('Yes')
        exit()
        
print('No')