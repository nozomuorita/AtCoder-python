"""
・和が10の倍数でないなら、そのまま出力
・10の倍数ならsを小さいほうから見て、10の倍数でない数字ならそれを引いて答え
・10の倍数でないものがないなら不可なので、0と表示
"""
n = int(input())
s = [int(input()) for _ in range(n)]
s.sort()

ss = sum(s)

if ss%10!=0: print(ss)
else:
    while s:
        t = s.pop(0)
        if t%10!=0:
            exit(print(ss-t))
    
    print(0)