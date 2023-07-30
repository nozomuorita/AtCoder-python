n = int(input())
n_list = [i for i in range(1, 2*n+1+1)] # 宣言できる数字のリスト
said = [False] * (2*n+1+1) # すでに呼ばれた数字かどうか

f = True # ゲームが終わったかどうか

while f:
    # 宣言できる数字から一つ取り出す
    num = n_list.pop(0)
    
    # numがまだ呼ばれていないなら、出力し、saidをTrueにする
    if not(said[num]):
        print(num)
        said[num] = True
    # すでに呼ばれているなら、呼ばれていないものが見つかるまで繰り返す
    else:
        while (said[num]):
            num = n_list.pop(0)
        # 出力し、saidをTrueにする
        print(num)
        said[num] = True

    # 青木君の数字を受け取る
    aoki_num = int(input())
    # 0ならfをFalseとしてゲーム終了
    if aoki_num == 0:
        f = False
    # 0でないならば、saidに入れる
    else:
        said[aoki_num] = True