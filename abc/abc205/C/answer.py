a, b, c = map(int, input().split())

# cが偶数の場合、a, bの符号が逆であっても結果は同じ
if c%2 == 0:
    if abs(a) < abs(b):
        print('<')
    elif abs(a) == abs(b):
        print('=')
    else:
        print('>')
# cが奇数の場合、a, bの大小がそのまま答えとなる
else:
    if a < b:
        print('<')
    elif a == b:
        print('=')
    else:
        print('>')