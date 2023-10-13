"""
・答えで二分探索を行う(長さがans以上のk+1個のピースに分割できるか)
"""

n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))

# 各ピース間の差分を計算しておく
a2 = [a[0]]
for i in range(1, n):
    a2.append(a[i]-a[i-1])
a2.append(l-a[-1])

left = 0
right = l

while (right-left)>1:
    mid = (left+right)//2                                    # mid以上のk+1個のピースに分割できるか

    # 愚直にmid以上になるように分割していく
    piece = 0                                                # ピースの長さ
    piece_num = 1                                            # 分割したピースの数(最初は分割していないのでピースは1個)
    for i in range(n+1):
        if piece_num==k+1:                                   # ピースがk+1個に分割できたなら残りのピースは足すだけ(k+1個以上に分割しないように)
            piece += a2[i]
        else:
            if piece+a2[i]<mid:                              # ピースを足してもmidに届かないなら足す
                piece += a2[i]
            else:                                            # ピースを足した時にmidを超えるならそこで分割する
                piece = 0                                    # pieceを0にリセット(pieceは次の分割に使うため)
                piece_num += 1                               # 分割したらピースの数は1増えるのでインクリメント
    
    if (piece_num<k+1) or (piece_num==k+1 and piece<mid):    # 操作後にピースの数がk+1に満たないか、k+1個に分割したが最後のピースがmid以上になっていないならばmid以上に分割することは不可なのでrightを移動
        right = mid
    else:                                                    # elseならmid以上に分割可能なのleftを移動
        left = mid
        
print(left)