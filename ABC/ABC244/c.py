n = int(input())
n_list = [i for i in range(1, 2*n+1+1)]
said = [False] * (2*n+1+1)

f = True

while f:
    num = n_list.pop(0)
    
    # numがまだ呼ばれていないなら、宣言
    if not(said[num]):
        print(num)
        said[num] = True
    # すでに呼ばれているなら、呼ばれていないものになるまで繰り返す
    else:
        while (said[num]):
            num = n_list.pop(0)
        print(num)
        said[num] = True

    aoki_num = int(input())
    if aoki_num == 0:
        f = False
    else:
        said[aoki_num] = True