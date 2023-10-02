"""
・重実装
・aのポリオミノの向きを固定して、b、cを回転させたものを置けるのか判定
・1. b、cのポリオミノの向きを決定
・2. a, b, cを4*4のマス内に置けるのか全探索
"""
a = [list(input()) for _ in range(4)]
b = [list(input()) for _ in range(4)]
c = [list(input()) for _ in range(4)]

# ポリオミノpを(x, y)を左上として置く関数
# おけない場合は、falseを返す
# p: 置きたいポリオミノ
# x, y: 起点、(x, y)が最も左上に来るように置く
# pol: ベースとなるポリオミノ、このpolに対して、pを置いていく
# ex) サンプル１について
# put(a, 0, 0, pol)とした場合を考える(polは4*4ですべて'.'の二次元配列)
# このとき、出力はaの(1, 0)の'#'が(0, 0)に来るように配置したものとなる.(x, y)に詰めて配置するということ
def put(p, x, y, pol):
    # (x, y)が枠外ならば、おくことはできない(False)
    if x<0 or x>=4 or y<0 or y>=4:
        return False
    
    first = True
    bx, by = -1, -1
    for i in range(4):
        for j in range(4):
            if p[i][j]=='#':
                # 最初に見つけた'#'は、最も左上にあるので、これを(x, y)に置く
                if first:
                    bx = i
                    by = j
                    first = False
                    if pol[x][y]!='#':
                        pol[x][y] = '#'
                # 以降、見つけたものについては、最初に置いたものとの差分を計算して(x, y)を基準に配置
                else:
                    x2 = x+(i-bx)
                    y2 = y+(j-by)
                    # 今から置く座標が範囲外であるか、すでに'#'が置かれているならばFalse、そうでないなら置く
                    if 0<=x2<4 and 0<=y2<4 and pol[x2][y2]!='#':
                        pol[x2][y2] = '#'
                    else:
                        return False
    return pol

# ポリオミノpを回転させる(deg: 0=回転なし、1=90°左回転、2=90°右回転、3=180°回転)
def rotate(p, deg):
    # 回転なしならそのまま返す
    if deg==0:
        return p
    # 90°左回転
    elif deg==1:
        #  90°左回転は、転置してから上下逆にする
        tp = []
        transposed = list(zip(*p))
        for i in transposed[::-1]:
            tp.append(list(i))
        return tp
    # 90°右回転
    elif deg==2:
        # 90°右回転は、上下逆にしてから転置する
        tp = []
        for i in p[::-1]:
            tp.append(i)
        tp = list(zip(*tp))
        tp2 = [list(i) for i in tp]
        return tp2
    # 180°回転
    elif deg==3:
        #  180°回転なら、左右逆にしてから上下逆
        tp = []
        for i in p[::-1]:
            tp.append(i[::-1])
        return tp                
    
# 最初の二つのfor文で、ポリオミノbとポリオミノcの向きを決定
for p2_r in range(4):  # polyomino2の向き
    p2 = rotate(b, p2_r)
    for p3_r in range(4):  # polyomino3の向き
        p3 = rotate(c, p3_r)
        # ポリオミノa、ポリオミノb、ポリオミノcを置く位置を全通り試す
        # (i, j)=ポリオミノaを置く位置
        # (i2, j2)=ポリオミノbを置く位置
        # (i3, j3)=ポリオミノcを置く位置
        for i in range(4):
            for j in range(4):
                for i2 in range(4):
                    for j2 in range(4):
                        for i3 in range(4):
                            for j3 in range(4):
                                polyomino = [['.']*4 for _ in range(4)]     # 最初は、すべて'.'とする
                                polyomino = put(a, i, j, polyomino)         # ポリオミノaを置く
                                if polyomino!=False:                        # ポリオミノがFasleでない=ポリオミノaを置くことができたならbを置く
                                    polyomino = put(p2, i2, j2, polyomino)
                                if polyomino!=False:                        # ポリオミノがFalseでない=a, bを置くことができたならcを置く
                                    polyomino = put(p3, i3, j3, polyomino)
                                #print(polyomino)
                                if polyomino==False:                        # polyominoがFalseなら、置くことができていないので飛ばす
                                    continue
                                else:                                       # Falseでないなら、ポリオミノがすべて埋まっているか確認
                                    count = 0
                                    for idx in polyomino:
                                        count += idx.count('#')
                                    if count==16:                           # '#'を数えて、16個あれば、埋めることができているのでYesとして終了
                                        print('Yes')
                                        exit()
print('No')