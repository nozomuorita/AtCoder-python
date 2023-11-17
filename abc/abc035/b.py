"""
・文字列の順番は関係ないので、先に"?"以外を見て、移動後の位置を計算(x, yとする)
・最大値を求める場合
・プラスにしろマイナスにしろ"?"の分だけ遠い方に移動するのが良いため、ans=abs(x)+abs(y)+(?の数)
・最小値の場合
・abs(x)+abs(y)より"?"の数が小さいなら"?"の分だけ原点に近づくのが最適、ans=abs(x)+abs(y)-(?の数)
・"?"の数がabs(x)+abs(y)より大きい場合、まず原点に行くことはできる
・原点に行く移動した後、残っている"?"は、(?の数)-(abs(x)+abs(y))となる
・残った"?"の数が偶数なら、原点に戻ることができる(+1してから-1など)ためans=0
・奇数なら原点から1回移動した場所となる。ans=1
"""
s = list(input())
t = int(input())

s.sort(reverse=True)
x, y = 0, 0
for i in range(len(s)):
    if s[i]=="?": break
    if s[i]=="L": x-=1
    elif s[i]=="R": x+=1
    elif s[i]=="U": y+=1
    else: y-=1

if t==1: print(abs(x)+abs(y)+(len(s)-i))
else:
    h = len(s) - i
    dist = abs(x) + abs(y)
    if dist>=h: print(dist-h)
    else:
        h -= dist
        print(0) if h%2==0 else print(1)