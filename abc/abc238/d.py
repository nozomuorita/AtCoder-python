T = int(input())

for _ in range(T):
    a, s = map(int, input().split())

    x, y = 0, 0
    # aが1であるビットはxとyに加算する
    for i in range(61):
        if a>>i & 1: x+=2**i; y+=2**i
    
    # 桁の大きいほうから見ていく
    # aのiビット目が0のとき、ありうるのは(1, 0)か(0, 0)である
    # xに1を立てた時に、x+yがsを超えるなら立てることはできないので(0, 0)とする。
    # 超えないならxに1を立てる
    # 全ビットについて行ったときに、x+y==sとできるならyes
    for i in range(61, -1, -1):
        if not(a>>i & 1):
            if (x+(2**i)+y)<=s: x+=2**i
    
    print('Yes') if x+y==s else print('No')